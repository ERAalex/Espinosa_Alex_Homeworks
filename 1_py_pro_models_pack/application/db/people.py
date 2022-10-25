from main import conn
import psycopg2.extras
from flask import request, flash

# Woring with DB



# show or clients on our employees.html
def change_client_get():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM employees"
    cur.execute(s)  # Execute the SQL
    list_users = cur.fetchall()
    return list_users


# create new employees
def upload_new_client():
    if request.method == 'POST':
        # id = request.form['id_f']
        name = request.form['name_f']
        surname = request.form['surname_f']
        email = request.form['email_f']
        salary = request.form['salary_f']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            INSERT INTO employees
            (name, surname, email, salary_total)
            VALUES (%s,%s,%s,%s)
        """, (name, surname, email, salary))
        conn.commit()
        return flash('База успешно обновлена, E.R.Alex')


# i need id to know what data to delete (it's a name-row {0} in out template - employees)
def delete_client(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DELETE FROM employees WHERE id = {0}'.format(id))
    conn.commit()
    return flash('Клиент успешно удален из базы')


# find some person to edit.
def change_client_new_info_p(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('SELECT * FROM employees WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    article_show = data[0]
    return article_show



# change person information when we have just find it
def final_change_person_p(id):
    if request.method == 'POST':
        name_b = request.form['name']
        surname_b = request.form['surname']
        email_b = request.form['email']
        salary_b = request.form['salary']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE employees
            SET name = %s,
                surname = %s,
                email = %s,
                salary_total = %s
            WHERE id = %s
        """, (name_b, surname_b, email_b, salary_b, id))
        result_frase = 'ok'
        conn.commit()
        return result_frase



