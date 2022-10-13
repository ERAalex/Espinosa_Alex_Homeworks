import json
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Stock
import pandas as pd


# connection block
login = os.getenv('login_db')
passw = os.getenv('passw_db')
db_name = os.getenv('db_name_a')

DSN = f'postgresql://{login}:{passw}@localhost:5432/{db_name}'
engine = sqlalchemy.create_engine(DSN)

# for connection and woking we need 'sessions' - it's like using cursor
Session = sessionmaker(bind=engine)
session = Session()


# create_tables(engine)


#
# __________ IMPORT BLOCK  JSON  -  PANDAS  -  SQL ____________#
#
# # We can use library Pandas to put information on DB, it's quite simple, and it's required at work to know Pandas
# just open json with our table
#
# with open('publisher.json', 'r') as f:
#     data = json.load(f)
#     # preparing data for pd.  pd -it's Panda
#     df = pd.DataFrame(data)
#     # publisher -it's a name of out table where we need to put some information, df.to_sql -we put our information in DB
#     df.to_sql('publisher', engine, index=False, if_exists='append')
#
# with open('book.json', 'r') as f:
#     data = json.load(f)
#     df = pd.DataFrame(data)
#     df.to_sql('book', engine, index=False, if_exists='append')
#
# with open('shop.json', 'r') as f:
#     data = json.load(f)
#     df = pd.DataFrame(data)
#     df.to_sql('shop', engine, index=False, if_exists='append')
#
# with open('stock.json', 'r') as f:
#     data = json.load(f)
#     df = pd.DataFrame(data)
#     df.to_sql('stock', engine, index=False, if_exists='append')
#
# with open('sale.json', 'r') as f:
#     data = json.load(f)
#     df = pd.DataFrame(data)
#     df.to_sql('sale', engine, index=False, if_exists='append')





# because it's just like cursor we need to close it at the end of working
session.close()
