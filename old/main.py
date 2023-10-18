# This is a sample Python script.
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PySimpleGUI as sg;
from picore import *
import requests as rq
import sys
import types
import httpx
import asyncio

# print(f'Connecting to {SERVER_ENDPOINT}...')

apis = {
    # 'test'  : 'api/test',
    # 'swap'  : 'api/swap',
    'play'  : 'Play',
    'cancel': 'Stop'

}
c = httpx.AsyncClient()
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.

rq.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


async def main():
    # Define the window's contents
    output_ = '-OUTPUT-'
    rc: int = 0

    mypath = r"H:\Other Music\Audio resources\NMicspam"
    files = get_files(mypath)
    rg = []
    for i in range(len(files)):
        rg.append((i, files[i]))

    listbox = sg.Listbox(values=rg, size=(50, 35), key='lb', select_mode=sg.SELECT_MODE_SINGLE, enable_events=True)
    layout = [
        [sg.Text(f"{SERVER_ENDPOINT}"), sg.Text(f"{rc}", key='api')],
        map(lambda x: sg.Button(x), apis.keys()),
        [listbox],
        [sg.Text(f"...", key=output_)]
    ]

    window = sg.Window('PiCore', layout)
    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Ok':
            break
        output = None

        if event in apis:

            if event == 'play':
                lb_ = values['lb'][0][1]
                lb_ = os.path.join(mypath, lb_)
                re = rq.request('GET', f'{SERVER_ENDPOINT}/{apis[event]}', headers={'s': lb_}, verify=False)
                output = re.text
            elif event == 'cancel':
                lb_ = values['lb'][0][1]
                lb_ = os.path.join(mypath, lb_)
                re = rq.request('GET', f'{SERVER_ENDPOINT}/{apis[event]}', headers={'s': lb_}, verify=False)
                output = re.text
            else:
                re = rq.request('GET', f'{SERVER_ENDPOINT}/{apis[event]}', verify=False)
                output = re.text

        # else:
        #     pass

        print((event, values))

        if output:
            window[output_].update(output)

    # Finish up by removing from the screen
    window.close()


if __name__ == '__main__':
    asyncio.run(main())
