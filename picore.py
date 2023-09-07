from os import listdir
import os
from os.path import isfile, join

PORT: int = 5003

endpoint_actions_map = {
    'test': 'api/test',
    'swap': 'api/swap'
}

SC_OK: int = 200
REMOTE = "192.168.1.79"
SERVER_ENDPOINT = f'http://{REMOTE}:{PORT}'


def get_files(mypath):

    onlyfiles = [f for (dirpath, dirnames, filenames) in os.walk(mypath) for f in filenames]
    return onlyfiles
