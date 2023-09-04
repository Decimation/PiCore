import requests
import argparse
import os
from picore import *

# Copy-Item .\client.py C:\Users\Deci\Desktop\RPi\ -Force

REMOTE = "192.168.1.79"
SERVER_ENDPOINT = f'http://{REMOTE}:{PORT}'


parser = argparse.ArgumentParser(prog='PiCoreClient')
actions = parser.add_argument('-action', choices=endpoint_actions_map.keys())
args = parser.parse_args()


def send_request():
    try:

        response = requests.get(f'{SERVER_ENDPOINT}/{endpoint_actions_map[args.action]}')
        if response.status_code == SC_OK:
            print('Server Response:', response.text)
        else:
            print('Error:', response.status_code)
    except Exception as e:
        print('An error occurred:', str(e))


if __name__ == '__main__':
    print(f'Connecting to {SERVER_ENDPOINT}...')
    send_request()
