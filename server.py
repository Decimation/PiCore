import os
import subprocess
from os import *
from flask import Flask
from flask import Response
from picore import *

HOST = '0.0.0.0'

app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def hello():
    return Response(status=SC_OK, response='Hello')


@app.route('/api/swap', methods=['GET'])
def swap():
    p = subprocess.run(['autohotkey', r"C:\Users\Deci\Documents\Computer Science\AHK Library\Alt+Ctrl+F11.ahk"])
    return Response(status=SC_OK, response=f'{p.stdout}')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
