

text_1 = '1.txt'
text_2 = '2.txt'
text_3 = '3.txt'

# вытаскиваем информацию из 1 файла
with open(text_1, encoding='utf-8') as f:
    first_txt = f.read().split('\n')
    f.close()

# вытаскиваем информацию из 1 файла
with open(text_2, encoding='utf-8') as f:
    second_txt = f.read().split('\n')
    f.close()

# вытаскиваем информацию из 1 файла
with open(text_3, encoding='utf-8') as f:
    third_txt = f.read().split('\n')
    f.close()

size_first = len(first_txt)
size_second = len(second_txt)
size_third = len(third_txt)

all_text = []

if size_first <= size_second and size_first <= size_third:
    all_text.append([text_1])
    all_text.append([first_txt])
    if size_second <= size_third:
        all_text.append([text_2])
        all_text.append([second_txt])
        all_text.append([text_3])
        all_text.append([third_txt])
    else:
        all_text.append([text_3])
        all_text.append([third_txt])
        all_text.append([text_2])
        all_text.append([second_txt])

if size_second <= size_first and size_second <= size_third:
    all_text.append([text_2])
    all_text.append([second_txt])
    if size_first <= size_third:
        all_text.append([text_1])
        all_text.append([first_txt])
        all_text.append([text_3])
        all_text.append([third_txt])
    else:
        all_text.append([text_3])
        all_text.append([third_txt])
        all_text.append([text_1])
        all_text.append([first_txt])

if size_third <= size_second and size_third <= size_first:
    all_text.append([text_3])
    all_text.append(third_txt)
    if size_second <= size_first:
        all_text.append([text_2])
        all_text.append([second_txt])
        all_text.append([text_1])
        all_text.append([first_txt])
    else:
        all_text.append([text_1])
        all_text.append([first_txt])
        all_text.append([text_2])
        all_text.append([second_txt])


with open('result.txt', 'a', encoding='utf-8') as f:

    f.write(str(all_text[0]) + '\n' + str(len(all_text[1])) + '\n')
    for item in all_text[1]:
        f.write(str(item) + '\n')

    f.write(str(all_text[2]) + '\n' + str(len(all_text[3])) + '\n')
    for item in all_text[3]:
        f.write(str(item) + '\n')

    f.write(str(all_text[4]) + '\n' + str(len(all_text[5])) + '\n')
    for item in all_text[5]:
        f.write(str(item) + '\n')

    f.close()
