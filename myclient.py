import requests
import sys

def read_input() -> str:
    for line in sys.stdin:
        return line

if __name__ == '__main__':
    
    while True:
        # print text on console
        # input choice
        # input amount
        print('1. FXConverter')
        print('2. USDConverter')
        choice = int(read_input())
        print('Amount? ')
        amount = int(read_input())
        # query http with choice and amount
        http_query = f'http://localhost:8000/converter?choice={choice}&amount={amount}'
        payload = {}
        headers = {}
        response = requests.request("GET", http_query, headers=headers, data=payload)
        # display the result in the console
        print(response.text)








