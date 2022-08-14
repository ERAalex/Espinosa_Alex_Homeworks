
all_files = ['1.txt', '2.txt', '3.txt']
dict_text = {}
size_text = {}
for item in all_files:
    with open(item, encoding='utf-8') as f:
        first_txt = f.read().split('\n')
        size = len(first_txt)
        all_text.append(item)
        dict_text[size] = first_txt
        size_text[size] = item

sorted_size_dic = dict(sorted(size_text.items()))
print(sorted_size_dic)

with open('result.txt', 'a', encoding='utf-8') as f:
    for key, value in sorted_size_dic.items():
        f.write(str(key) + '\n' + value + '\n')
        for k, value in dict_text.items():
            if k == key:
                for item in value:
                    f.write(item + '\n')
    f.close()