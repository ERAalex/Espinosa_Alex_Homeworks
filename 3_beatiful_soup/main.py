from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint


# добавил слов, чтобы больше статей выводило
keywords = ['дизайн', 'фото', 'web', 'Python', 'История', 'споры', 'арест']

src = requests.get('https://habr.com/ru/all/').text

# Так как блочил сайт, из-за большого количества запросов, сделал html шаблон копию сайта, чтобы на нем тестить
# with open("test.html", encoding='utf-8') as file:
#     src = file.read()


soup_t = bs(src, features='html.parser')


result_sec = soup_t.find("div", class_="tm-articles-list").find_all("article", class_="tm-articles-list__item")

data_result = []

for item in result_sec:
    name_art_find = item.find("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2").\
        find("a", class_="tm-article-snippet__title-link").find("span").text


    for item_word in keywords:
        if item_word in name_art_find:
            time_find = item.find("div", class_="tm-article-snippet__meta-container").\
                find("div", class_="tm-article-snippet__meta").find("span", class_="tm-article-snippet__datetime-published").\
                find("time")
            time_result = time_find['datetime']

            link_find = item.find("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2").\
                find("a", class_="tm-article-snippet__title-link")
            link_result = 'https://habr.com' + link_find['href']

            data_result.append((time_result + ' - ' + name_art_find + ' - ' + link_result))


for item_data in data_result:
    print(item_data)

