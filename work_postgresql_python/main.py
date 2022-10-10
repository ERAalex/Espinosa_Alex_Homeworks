import psycopg2

conn = psycopg2.connect(database="python_netology", user="alex", password="nazca007")

cur = conn.cursor()


# создание таблицы Person функция, подается курсор + название для таблицы
# CONSTRAINT surname_unique UNIQUE (surname) - избавляемся от возможности дублежа фамилии
def create_t(cursor, name_t):
        cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {name_t}(
                id SERIAL PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(40),
                surname VARCHAR(40),
                email VARCHAR(40),
                CONSTRAINT surname_unique UNIQUE (surname)  
                );
                """)
        return conn.commit()

create_t(cur, name_t = 'person')

# создание таблицы функция для телефонов, подается курсор + название для таблицы
def create_ph(cursor, name_t):
        cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {name_t}(
                id SERIAL PRIMARY KEY,
                number integer,
                person_id int REFERENCES person (id) ON UPDATE CASCADE ON DELETE CASCADE,
                CONSTRAINT number_unique UNIQUE (number)  
                );
                """)
        return conn.commit()

# create_ph(cur, name_t = 'phone_numbers')

def new_person(cursor, name_p, surname_p, email_p):
        cursor.execute(f"""
        INSERT INTO person (id, name, surname, email)
        VALUES (3, '{name_p}', '{surname_p}', '{email_p}') RETURNING id, name;
        """)

        return conn.commit()

# new_person(cur, name_p='James, surname_p='Stivens', email_p='dss@ksds.ru')

# new_person(cur, name_p='jeje')