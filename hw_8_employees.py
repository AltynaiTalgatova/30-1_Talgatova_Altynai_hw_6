# 5. Создать таблицу employees (сотрудники) c колонками id первичный ключ автоинкрементируемый,
# колонка first_name (имя) с текстовым не пустым значением,
# колонка last_name (фамилия) с текстовым не пустым значением,
# а также колонка city_id с внешним ключом на таблицу cities.
# 6. Добавить 15 сотрудников проживающих в разных городах.
# В пунктах с 1го по 6й можно использовать любой вариант для работы в СУБД SqlLite
# (Из кода в Python или SQL запросами или через любую программу с графическим интерфейсом для управления БД).
# 7. Написать программу в Python, которая при запуске бы отображала фразу
# “Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже,
# для выхода из программы введите 0:”
# 8. Ниже фразы программа должна распечатывать список городов из вашей базы данных следующим образом
# Бишкек
# Ош
# Берлин
# Пекин
# и тд…
# 9. После ввода определенного id города программа должна найти всех сотрудников из вашей базы данных
# проживающих в городе выбранного пользователем и отобразить информацию о них в консоли
# (Имя, фамилия, страна и город проживания)

import sqlite3

def create_connection(hw8):
    conn = None
    try:
        conn = sqlite3.connect(hw8)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_employee(conn, employee):
    try:
        sql = '''INSERT INTO employees (first_name, last_name, city_id) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, employee)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


employee_name = 'hw8.db'
create_employees_table_sql = \
    '''CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL,
    city_id INTEGER NOT NULL, 
    FOREIGN KEY (city_id) REFERENCES cities (id)
    )'''


connection = create_connection(employee_name)
if connection is not None:
    print("Successfully connected!")
    create_table(connection, create_employees_table_sql)
    insert_employee(connection, ('Chanyeol', 'Park', 2))
    insert_employee(connection, ('Yixing', 'Zhang', 3))
    insert_employee(connection, ('Baekhyun', 'Byun', 2))
    insert_employee(connection, ('Yuko', 'Vatanabe', 6))
    insert_employee(connection, ('Alice', 'Gilbert', 2))
    insert_employee(connection, ('Midoriya', 'Izuku', 6))
    insert_employee(connection, ('Markus', 'Walker', 6))
    insert_employee(connection, ('Alexander', 'Black', 4))
    insert_employee(connection, ('Liam', 'Holmes', 7))
    insert_employee(connection, ('Sakura', 'Ito', 3))
    insert_employee(connection, ('Kyungsoo', 'Do', 4))
    insert_employee(connection, ('Minho', 'Lee', 7))
    insert_employee(connection, ('Caroline', 'Forbes', 1))
    insert_employee(connection, ('Chris', 'King', 5))
    insert_employee(connection, ('Xiatian', 'Jin', 1))
    connection.close()
