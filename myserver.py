import http.server
import socketserver

from myconverter import SelectConverter
from urllib.parse import urlparse, parse_qs

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        # get choice from query        
        # get amount from query
        urlparsed = urlparse(self.path)
        queryparsed = parse_qs(urlparsed.query)
        choice, amount = queryparsed['choice'][0], queryparsed['amount'][0]
        # use select converter with given choice
        converter = SelectConverter.get_converter(int(choice))
        # use converter to convert amount
        result = converter.convert(int(amount))
        # return amount converted
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response = f'Your choice was {choice} and your amount was {amount}, the result is {result}'
        response = 'Your choice was {0} and your amount was {1} {3}, the result is {2} {4}'.format(choice, amount, result, converter.from_currency, converter.to_currency)
        print('{choice} {amount} => {result2}'.format(choice=choice, amount=amount, result2=result))
        self.wfile.write(str.encode(response)) #Response to the client

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()