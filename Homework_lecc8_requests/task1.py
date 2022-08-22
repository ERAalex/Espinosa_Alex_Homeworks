import requests
from pprint import pprint
import json
import operator


# Обращаемся к сайту, за json
def recive_req():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    res = requests.get(url)
    return res.json()

all_hero_data = recive_req()
dict_3_hero = {}

# достаем нужные параметры в свой словарь, сразу берем параметры по 3 героям.
for item in all_hero_data:
    if item['name'] == 'Captain America' or item['name'] == 'Hulk' or item['name'] == 'Thanos':
        dict_3_hero[item['name']] = item['powerstats']['intelligence']

sorted_3hero = dict(sorted(dict_3_hero.items(), key=operator.itemgetter(1))) # сортируем словарь по значениям
print(f'Самый умный герой из 3 - {list(sorted_3hero.keys())[-1]}')