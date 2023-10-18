import subprocess
from os import *
from flask import Flask, request
from flask import Response
from old.picore import *

import pyaudio
import wave

HOST = '0.0.0.0'

app = Flask(__name__)

p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)

    print((i, dev['name'], dev['maxInputChannels'], dev['maxOutputChannels']))
    # print((i, dev))


@app.route('/api/test', methods=['GET'])
def hello():
    return Response(status=SC_OK, response='Hello')


@app.route('/api/swap', methods=['GET'])
def swap():
    proc = subprocess.run(['autohotkey', r"C:\Users\Deci\Documents\Computer Science\AHK Library\Alt+Ctrl+F11.ahk"])
    return Response(status=SC_OK, response=f'{proc.stdout}')


running_audio = {}


@app.route('/api/cancel', methods=['GET'])
def cancel():
    try:
        sz = request.headers['s']
        sz = path.join(r"H:\Other Music\Audio resources\NMicspam", sz)
        if sz in running_audio:
            running_audio[sz].stop_stream()
            running_audio[sz].close()
            # p.close(running_audio[sz])
            running_audio.pop(sz)
        return Response(status=SC_OK, response=f'{sz}')
    except:
        return Response(status=SC_OK)


@app.route('/api/play', methods=['GET'])
def play():

    try:
        sz = request.headers['s']
        sz = path.join(r"H:\Other Music\Audio resources\NMicspam", sz)
        print(f">>{sz}")
        audio = wave.open(fr"{sz}", "rb")
        device = 10

        print(f"{device}")
        getnchannels = audio.getnchannels()

        s = p.open(output_device_index=device,
                   format=p.get_format_from_width(audio.getsampwidth()),
                   channels=getnchannels,
                   rate=audio.getframerate(),
                   output=True)

        # s = p.open(input_device_index=device,
        #            format=p.get_format_from_width(audio.getsampwidth()),
        #            channels=getnchannels,
        #            rate=audio.getframerate(),
        #            input=True)

        running_audio[sz] = s

        d = audio.readframes(1024)
        while d:
            s.write(d)
            d = audio.readframes(1024)

        s.stop_stream()
        s.close()

        return Response(status=SC_OK, response=f'{audio}')
    except:
        return Response(status=SC_OK)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
