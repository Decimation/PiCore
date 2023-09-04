from flask import Flask

PORT = 5003
HOST = '0.0.0.0'

app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def hello():
    return 'Hello from your PC!'


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
