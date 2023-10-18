from os import listdir
import os
from os.path import isfile, join

# PORT: int = 5003

PORT: int = 60900

SC_OK: int = 200
# REMOTE = "192.168.1.79"
REMOTE = "localhost"

SERVER_ENDPOINT = f'http://{REMOTE}:{PORT}'


def get_files(mypath):

    onlyfiles = [f for (dirpath, dirnames, filenames) in os.walk(mypath) for f in filenames]
    return onlyfiles
