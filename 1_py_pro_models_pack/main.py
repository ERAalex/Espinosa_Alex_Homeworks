from flask import Flask
from flask import render_template, url_for, request, flash, redirect
import os
import psycopg2
from application.db.people import *
from datetime import datetime

app = Flask(__name__)


secret_kk = os.getenv('SECR_KEY')
DB_USER = os.getenv('n_base_postgr')
DB_PASS = os.getenv('passw_base_postgr')
DB_NAME = os.getenv('name_db_postgr')


app.config['SECRET_KEY'] = secret_kk
if 'SECURITY_PASSWORD_SALT' not in app.config:
    app.config['SECURITY_PASSWORD_SALT'] = app.config['SECRET_KEY']


app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASS}@localhost:5432/{DB_NAME}'


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host="localhost")


UPLOAD_FOLDER = 'static/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    now_date = datetime.today().strftime("%d.%m.%Y")
    clock_date = datetime.today().strftime("%H:%M:%S")
    return render_template('index.html', now_date=now_date, clock_date=clock_date)



@app.route("/change_client")
def change_client_init():
    result = change_client_get()
    return render_template('employees.html', result=result)



@app.route("/change_client", methods=['POST'])
def change_client():
    result = upload_new_client()
    return redirect(url_for('change_client', result=result))


# i need id to know what data to delete (it's a name-row {0} in out template - employees)
@app.route("/delete_employee/<id>", methods=['POST', 'GET'])
def change_client_delete(id):
    result = delete_client(id)
    return redirect(url_for('change_client', result=result))


# find and go to page to have a posibility to change a person
@app.route("/change_client_new_info/<id>", methods=['GET'])
def change_client_new_info(id):
    result = change_client_new_info_p(id)
    return render_template('employees_upgrade.html', result=result)


@app.route("/change_client_new_info/<id>", methods=['POST', 'GET'])
def final_change_person(id):
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
    flash('Данные изменены, Espinosa Alex')
    conn.commit()
    return redirect(url_for('change_client_init'))




@app.route("/calculate_sal")
def calculate_sal():
    result = change_client_get()
    return render_template('calculate_sal.html', result=result)


@app.route("/calculate_sal_find/<id>", methods=['GET'])
def calculate_sal_find(id):
    result = change_client_new_info_p(id)
    return render_template('calculate_sal_count.html', result=result)





@app.route("/calculate_sal_find/<id>", methods=['POST', 'GET'])
def calculate_sal_give_money(id):
    name_b = request.form['name']
    surname_b = request.form['surname']
    email_b = request.form['email']
    salary_b = request.form['salary']

    days_b = request.form['days']
    price_b = request.form['price']

    price_count = int(days_b) * int(price_b) + int(salary_b)
    total_price = price_count

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""
        UPDATE employees
        SET name = %s,
            surname = %s,
            email = %s,
            salary_total = %s
        WHERE id = %s
    """, (name_b, surname_b, email_b, total_price, id))
    flash('Данные изменены, Espinosa Alex')
    conn.commit()
    return redirect(url_for('calculate_sal'))







if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')