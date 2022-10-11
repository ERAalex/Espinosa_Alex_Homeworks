import psycopg2

conn = psycopg2.connect(database="YOUR_name", user="PUT_SOMETHING", password="PUT_SOMETHING")
cur = conn.cursor()


# создание таблицы Person функция, подается курсор + название для таблицы
# CONSTRAINT surname_unique UNIQUE (surname) - избавляемся от возможности дублежа фамилии
def create_t():
        cur.execute("""
                CREATE TABLE IF NOT EXISTS person(
                id SERIAL PRIMARY KEY,
                name VARCHAR(40),
                surname VARCHAR(40),
                email VARCHAR(40),
                CONSTRAINT surname_unique UNIQUE (surname)  
                );
                """)
        print('Команда выполнена. База создана \n')
        return conn.commit()



# создание таблицы функция для телефонов, подается курсор + название для таблицы
def create_ph():
        cur.execute(f"""
                CREATE TABLE IF NOT EXISTS phone_numbers(
                id SERIAL PRIMARY KEY,
                number VARCHAR(13),
                person_id int REFERENCES person (id) ON UPDATE CASCADE ON DELETE CASCADE,
                CONSTRAINT number_unique UNIQUE (number)  
                );
                """)
        print('Команда выполнена. База создана \n')
        return conn.commit()



# создание нового клиента
def new_person():
        name_p = input('Введите Имя: ')
        surname_p = input('Введите Фамилию: ')
        email_p = input('Введите почтовый адрес: ')

        cur.execute("""
        INSERT INTO person (name, surname, email)
        VALUES (%s, %s, %s);
        """, (name_p, surname_p, email_p,))

        print(f'\n Клиент {name_p} успешно создан \n')
        return conn.commit()



# создание телефона с привязкой к id клиента( id можно узнать по команде)
def new_phone():
        phone_p = input('Введите телефон (пишите целиком например 8911334455): ')
        id_find = input('Напишите ID клиента (можно узнать через команду check_person_id) : ')

        cur.execute("""
        SELECT name FROM person WHERE id=%s;
        """, (id_find,) )
        try:
                print('Имя клиента:')
                print(cur.fetchone()[0])
        except TypeError:
                return print('\n ошибка, Вы ввели неправильный ID или такого человека нет в базе \n ')


        cur.execute(f"""
        INSERT INTO phone_numbers (number, person_id)
        VALUES (%s, %s);
        """, (phone_p, id_find))
        conn.commit()
        print('\n Телефон успешно создан \n')



# Функция для определения ID person
def check_person_id():
        data_find = input('Введите для поиска ID или фамилию, или почту, или телефон (пример - 89117861515): ')
        cur.execute("""
        SELECT p.id FROM person p 
        LEFT JOIN phone_numbers pn on pn.person_id = p.id 
        WHERE p.surname=%s OR p.email=%s OR pn.number=%s
        """, (data_find, data_find, data_find,))

        try:
                result = cur.fetchone()[0]
                return print(f'По Вашему запросу ID клиента: {result}')
        except TypeError:
                print('Клиент по таким данным не найден.')



# Функция, позволяющая изменить данные о клиенте
def change_person():
        decision = input('''выберите цифру, что Вы хотите изменить: 
        1. имя
        2. фамилия
        3. почту :
        ''')

        id_decision = input('введите id изменяемого человека (узнать можно путем команды: check_person_id (фамилия)): ')

        cur.execute("""
        SELECT name FROM person WHERE id=%s;
        """, (id_decision,) )
        try:
                print(cur.fetchone()[0])
        except TypeError:
                return print('ошибка, Вы ввели неправильный ID или такого человека нет в базе')


        if decision == '1':
                new_name = input('Введите новое имя: ')
                cur.execute("""
                UPDATE person
                SET name = %s
                WHERE id = %s;
                """, (new_name, id_decision))
                conn.commit()
                return print(f'Данные успешно изменены, новое имя: {new_name}')

        if decision == '2':
                new_surname = input('Введите новую фамилию: ')
                cur.execute("""
                UPDATE person
                SET surname = %s
                WHERE id = %s;
                """, (new_surname, id_decision))
                conn.commit()
                return print(f'Данные успешно изменены, новая фамилия: {new_surname}')

        if decision == '3':
                new_email = input('Введите новый email: ')
                cur.execute("""
                UPDATE person
                SET email = %s
                WHERE id = %s;
                """, (new_email, id_decision))
                conn.commit()
                return print(f'Данные успешно изменены, новый email: {new_email}')


# Функция для удаления номера из базы
def del_phone():
        phone_p = input('Введите телефон который Вы хотите удалить из базы: ')

        cur.execute("""
        DELETE FROM phone_numbers WHERE number=%s;
        """, (phone_p,))

        conn.commit()
        print('Телефон успешно удален')

# del_phone(cur)


# Функция для удаления клиента из базы
def del_person():
        person_del = input('Введите ID клиента, которого нужно удалить (узнать можно путем команды: check_person_id (фамилия)) : ')

        cur.execute("""
        DELETE FROM person WHERE id=%s;
        """, (person_del,))

        conn.commit()
        print('Клиент успешно удален')

# del_person(cur)



status = True

while status:
        print('''\nВведите код для изменения базы данных.
Для уточнения команд введите  help.\n''')
        dec = input()

        if dec == 'help':
                print('''
                create_t      - создание новой таблицы Клиентов
                create_ph     - создание новой таблицы Телефонов
                new_person    - создание нового Клиента
                new_phone     - создание нового телефона
                check_person_id - проверка id клиента
                change_person - изменить данные о клиенте
                del_phone     - удалить телефон из базы
                del_person    - удалить клиента из базы
                exit          - завершить программу
                ''')

        if dec == 'create_t':
                create_t()
        elif dec == 'create_ph':
                create_ph()
        elif dec == 'new_person':
                new_person()
        elif dec == 'new_phone':
                new_phone()
        elif dec == 'check_person_id':
                check_person_id()
        elif dec == 'change_person':
                change_person()
        elif dec == 'del_phone':
                del_phone()
        elif dec == 'del_person':
                del_person()
        elif dec == 'exit':
                exit()













