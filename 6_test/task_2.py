import requests
from pprint import pprint
import os
#

token = os.getenv('token')


def create_folder(token_g, fold_name):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token_g}'}
    response = requests.put(f'{URL}?path={fold_name}', headers=headers)
    return response

pprint(create_folder(token, 's2s'))

