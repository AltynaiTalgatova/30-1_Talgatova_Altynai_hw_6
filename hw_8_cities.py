# 3. Добавить таблицу cities (города) c колонками id первичный ключ автоинкрементируемый,
# колонка title с текстовым не пустым названием города
# и колонка area площадь города не целочисленного типа данных со значением по умолчанием 0,
# а также колонка country_id с внешним ключом на таблицу countries.
# 4. Добавить 7 городов различных стран

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


def insert_city(conn, city):
    try:
        sql = '''INSERT INTO cities (title, area, country_id) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, city)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


city_name = 'hw8.db'
create_cities_table_sql = \
    '''CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    area DOUBLE(10, 2) NOT NULL DEFAULT 0.0
    country_id INTEGER NOT NULL, 
    FOREIGN KEY (country_id) REFERENCES countries (id)
    )'''


connection = create_connection(city_name)
if connection is not None:
    print("Successfully connected!")
    create_table(connection, create_cities_table_sql)
    insert_city(connection, ('Shanghai', 6340.0, 1))
    insert_city(connection, ('Seoul', 605.2, 2))
    insert_city(connection, ('Beijing', 16410.54, 1))
    insert_city(connection, ('Tokio', 2193.96, 3))
    insert_city(connection, ('Guangzhou', 7248.86, 1))
    insert_city(connection, ('Osaka', 223.0, 3))
    insert_city(connection, ('Busan', 770.0, 2))
    connection.close()
