
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


if size_first <= size_second and size_first <= size_third:
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(text_1 + '\n' + str(size_first) + '\n')
        for item in first_txt:
            f.write(item + '\n')

        if size_second <= size_third:
            f.write(text_2 + '\n' + str(size_second) + '\n')
            for item in second_txt:
                f.write(item + '\n')
            f.write(text_3 + '\n' + str(size_third) + '\n')
            for item in third_txt:
                f.write(item + '\n')
        f.close()



if size_second <= size_first and size_second <= size_third:
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(text_2 + '\n' + str(size_second) + '\n')
        for item in second_txt:
            f.write(item + '\n')

        if size_first <= size_third:
            f.write(text_1 + '\n' + str(size_first) + '\n')
            for item in first_txt:
                f.write(item + '\n')
            f.write(text_3 + '\n' + str(size_third) + '\n')
            for item in third_txt:
                f.write(item + '\n')
        f.close()
else:
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(text_3 + '\n' + str(size_third) + '\n')
        for item in third_txt:
            f.write(item + '\n')

        if size_first <= size_second:
            f.write(text_1 + '\n' + str(size_first) + '\n')
            for item in first_txt:
                f.write(item + '\n')
            f.write(text_2 + '\n' + str(size_second) + '\n')
            for item in second_txt:
                f.write(item + '\n')
        else:
            f.write(text_2 + '\n' + str(size_second) + '\n')
            for item in second_txt:
                f.write(item + '\n')
            f.write(text_1 + '\n' + str(size_first) + '\n')
            for item in first_txt:
                f.write(item + '\n')
        f.close()


