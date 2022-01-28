import requests

from . import *

def get_branches():
    response = requests.get(_API_ENDPOINT + "branches/")
    
    if response.status_code == 200:
        print(response.json())