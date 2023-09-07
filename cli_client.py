import requests
import argparse
import os
from picore import *

# Copy-Item .\cli_client.py C:\Users\Deci\Desktop\RPi\ -Force




parser = argparse.ArgumentParser(prog='PiCoreClient')
actions = parser.add_argument('-action', choices=endpoint_actions_map.keys())
args = parser.parse_args()




