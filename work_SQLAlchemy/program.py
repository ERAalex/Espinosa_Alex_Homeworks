import os
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Stock, Sale


# connection block
login = os.getenv('login_db')
passw = os.getenv('passw_db')
db_name = os.getenv('db_name_a')

DSN = f'postgresql://alex:nazca007@localhost:5432/netolog_sqlalchemy_homework'
engine = sqlalchemy.create_engine(DSN)

# for connection and woking we need 'sessions' - it's like using cursor
Session = sessionmaker(bind=engine)
session = Session()



find = input('Введите имя издателя или название книги: ')

chek = 'dddd'

# we need some list (result-[]) to save results and see them later. And let's make a 'count' to check if we get some
# results o no. We need a list because it's really a problem to separate information if we get many results (for example)
# the book is selling not just in 1 shop.
result = []
count = 0
for t in session.query(Publisher, Book, Stock, Shop).\
        join(Book, Book.id_publisher == Publisher.id).\
        join(Stock, Stock.id_book == Book.id).\
        join(Shop, Shop.id == Stock.id_shop).\
        filter(or_(Publisher.name.like(f'%{find}%'), Book.title.like(f'%{find}%'))):
    count += 1
    result.append(t)

session.close()

if count == 0:
    print("Информация по запросу не найдена. Нет книг")
else:
    for x in range(count):
        print('\nПолная информация по книге + данные по доступным магазинам')
        for s in result[x]:
            print(s)

