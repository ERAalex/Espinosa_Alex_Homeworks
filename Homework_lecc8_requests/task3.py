import requests
from pprint import pprint
import json

def recive_req():
    res = requests.get('https://api.stackexchange.com//2.3/questions?todate=1660953600&order=desc&max=1661126400&sort=activity&tagged=python&site=stackoverflow')
    return res.json()

result = recive_req()

count = 0
dict_of_questions = {}
for x in result['items']:
    count += 1
    dict_of_questions[count] = x['link']

print(f'всего вопросов по Python - {count}, за последние дни, все ссылки можно посмотреть в словаре')
