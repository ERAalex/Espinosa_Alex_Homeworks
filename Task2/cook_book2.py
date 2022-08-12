

################______ TASK №1 ______################

cook_book = {}

def book_c(f, count):
    start = 0
    list_ing = []
    while start <= count:
        count -= 1
        line = f.readline().split('|')
        if len(line) == 3:
            books = {}
            books['ingredient_name'] = line[0].strip('\n')
            books['quantity'] = line[1].strip('\n')
            books['measure'] = line[2].strip('\n')
            list_ing.append(books)
    return list_ing



with open('recipes2.txt', encoding='utf-8') as f:
    a = True
    while a:
        try:
            name = f.readline().strip('\n')
            count = int(f.readline())
            cook_book[name] = book_c(f, count)
        except:
            print('File is readed')
            a = False
            f.close()

print(f'result: {cook_book}\n')




################______ TASK №2 ______################

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for item in dishes:
        for key, value in cook_book.items():
            if item == key:
                for items in value:
                    for key, value in items.items():
                        if key == 'ingredient_name':
                            result[value] = items
    for key, value in result.items():
        if 'ingredient_name' in value:
            value.pop('ingredient_name')
    for key, value in result.items():
        for key, items in value.items():
            if key == 'quantity':
                value[key] = int(items)*int(person_count)
    print(f'для приготовления блюд {dishes} на {person_count} персон Вам надо: \n {result}')


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


################______ TASK №3 ______################




