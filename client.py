import requests

# Copy-Item .\client.py C:\Users\Deci\Desktop\RPi\ -Force

REMOTE = "192.168.1.79"
PORT = "5003"

SERVER_ENDPOINT = f'https://{REMOTE}:{PORT}'

def send_request():
    try:
        response = requests.get(f'{SERVER_ENDPOINT}/api/hello')
        if response.status_code == 200:
            print('Server Response:', response.text)
        else:
            print('Error:', response.status_code)
    except Exception as e:
        print('An error occurred:', str(e))


if __name__ == '__main__':
    send_request()
