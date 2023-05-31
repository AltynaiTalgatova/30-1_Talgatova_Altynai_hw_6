# ДЗУрок8 ДЭДЛАЙН 31.05.2023 23 59
# 1. Создать таблицу countries (страны) c колонками id первичный ключ автоинкрементируемый
# и колонка title с текстовым не пустым названием страны.
# 2. Добавить 3 записи в таблицу countries

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


def insert_country(conn, country):
    try:
        sql = '''INSERT INTO countries (title) VALUES (?)'''
        cursor = conn.cursor()
        cursor.execute(sql, country)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


country_name = 'hw8.db'
create_countries_table_sql = \
    '''CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL
    )'''


connection = create_connection(country_name)
if connection is not None:
    print("Successfully connected!")
    create_table(connection, create_countries_table_sql)
    insert_country(connection, ('China'))
    insert_country(connection, ('South Korea'))
    insert_country(connection, ('Japan'))
    connection.close()
