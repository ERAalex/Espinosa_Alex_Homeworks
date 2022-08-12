
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
    while
    name = f.readline().strip('\n')
    print(name)
    count = int(f.readline())
    cook_book[name] = book_c(f, count)
    print(f.readline())
