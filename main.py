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
    'test'  : 'api/test',
    'swap'  : 'api/swap',
    'play'  : 'api/play',
    'cancel': 'api/cancel'

}
c = httpx.AsyncClient()


async def main():
    # Define the window's contents
    output_ = '-OUTPUT-'
    rc: int = 0

    files = get_files(r"H:\Other Music\Audio resources\NMicspam")
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
                def play():
                    try:
                        # for i in window['lb'].get_indexes():
                        #     print(rg[i])
                        lb_ = values['lb'][0][1]
                        re = rq.request('GET', f'{SERVER_ENDPOINT}/api/play', headers={'s': lb_})
                        output = re.text
                        return output
                    except:
                        return

                rc += 1
                window['api'].update(f"{rc}")
                window.perform_long_operation(play, "play done")
            elif event == 'cancel':
                lb_ = values['lb'][0][1]
                re = rq.request('GET', f'{SERVER_ENDPOINT}/{apis[event]}', headers={'s': lb_})
                output = re.text
            else:
                re = rq.request('GET', f'{SERVER_ENDPOINT}/{apis[event]}')
                output = re.text

        if event == 'play done':
            rc -= 1
            window['api'].update(f"{rc}")

        # else:
        #     pass

        print((event, values))

        if output:
            window[output_].update(output)

    # Finish up by removing from the screen
    window.close()


if __name__ == '__main__':
    asyncio.run(main())
