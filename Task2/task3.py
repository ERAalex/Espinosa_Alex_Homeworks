import os

# код для поиска всех документов нужных для записи в 1.
# например у нас есть папка text_to_find мы в нее кидаем любое количество txt файлов для объединения по размеру и все

tree = os.walk('text_to_find')
all_files = []

for files in tree:
    for items in files:
        for inside_items in items:
            if inside_items.endswith('.txt'):
                all_files .append(inside_items)

dict_text = {}
size_text = {}
all_text = []

for item in all_files:
    # обязательно ставим путь до файла, т.к. код программа не в папке сейчас находится (в папке где файлы)
    with open(f'text_to_find/{item}', encoding='utf-8') as f:
        first_txt = f.read().split('\n')
        size = len(first_txt)
        all_text.append(item)
        dict_text[size] = first_txt
        size_text[size] = item


with open('result.txt', 'a', encoding='utf-8') as f:
    for key, value in sorted(size_text.items()):
        f.write(value + '\n' + str(key) + '\n')
        for k, value in dict_text.items():
            if k == key:
                for item in value:
                    f.write(item + '\n')
