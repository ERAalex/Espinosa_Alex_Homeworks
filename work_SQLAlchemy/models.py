import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

# making Base class for models, we make it using function declarative_base()
# this class can registrate all objects and later make tables
Base = declarative_base()


#let's make some tables.
class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'ID издателя - {self.id} | имя издателя - {self.name}'

class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    publisher = relationship(Publisher, backref='books')

    def __str__(self):
        return f'ID книги - {self.id} | название книги - {self.title}'

class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)


    def __str__(self):
        return f'ID магазина - {self.id} | название магазина - {self.name}'

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)

    book = relationship(Book, backref='stocks')
    shop = relationship(Shop, backref='stocks')


    def __str__(self):
        return f'ID stock: {self.id} | всего доступно книг для продажи: {self.count}'

class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.String(length=40))
    date_sale = sq.Column(sq.DateTime)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref='sales')


    def __str__(self):
        return f'{self.id}'



# now we have to made function to create this tables, and like cursor we use engine
def create_tables(engine):
    # if we need to delete some existing table and make the same but without any information, than use:
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
# after creating this function we can use it in settings.py
