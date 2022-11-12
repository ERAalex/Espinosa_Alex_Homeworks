import requests
from pprint import pprint
import json



token = 'y0_AgAAAABU48rYAAhViQAAAADMh1IKp3b8VZPgQ_C7kBP8muK0JUadra8'

def create_folder(token_g, fold_name):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token_g}'}
    response = requests.put(f'{URL}?path={fold_name}', headers=headers)
    return response

pprint(create_folder(token, 's2s'))

