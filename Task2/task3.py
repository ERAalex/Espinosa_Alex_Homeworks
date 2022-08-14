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

print(all_files)



dict_text = {}
size_text = {}
all_text = []

for item in all_files:
    with open(item, encoding='utf-8') as f:
        first_txt = f.read().split('\n')
        size = len(first_txt)
        all_text.append(item)
        dict_text[size] = first_txt
        size_text[size] = item

sorted_size_dic = dict(sorted(size_text.items()))

with open('result.txt', 'a', encoding='utf-8') as f:
    for key, value in sorted_size_dic.items():
        f.write(str(key) + '\n' + value + '\n')
        for k, value in dict_text.items():
            if k == key:
                for item in value:
                    f.write(item + '\n')
    f.close()