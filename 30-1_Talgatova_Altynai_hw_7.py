# ДЗУрок7 28.05.2023 23 59
# ДЗ*:
# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
# 2. В БД создать таблицу products
# 3. В таблицу добавить поле id - первичный ключ тип данных числовой и поддерживающий авто-инкрементацию.
# 4. Добавить поле product_title текстового типа данных максимальной длиной 200 символов,
# поле не должно быть пустым (NOT NULL)
# 5. Добавить поле price не целочисленного типа данных размером 10 цифр из которых 2 цифры после плавающей точки,
# поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0.0
# 6. Добавить поле quantity целочисленного типа данных, поле не должно быть пустым (NOT NULL) значением
# по-умолчанию поля должно быть 0
# 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров
# 8. Добавить функцию, которая меняет количество товара по id
# 9. Добавить функцию, которая меняет цену товара по id
# 10. Добавить функцию, которая удаляет товар по id
# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
# 12. Добавить функцию, которая бы выбирала из БД товары которые дешевле 100 сомов и количество которых
# больше чем 5 и распечатывала бы их в консоли
# 13. Добавить функцию, которая бы искала в БД товары по названию (Например: искомое слово “мыло”,
# должны соответствовать поиску товара с названием - “Жидкое мыло с запахом ванили”, “Мыло детское” и тд.)
# 14. Протестировать каждую написанную функцию


import sqlite3


def create_connection(hw):
    conn = None
    try:
        conn = sqlite3.connect(hw)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_product(conn, product):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_price_and_quantity_limit(conn, price_limit, quantity_limit):
    try:
        sql = '''SELECT * FROM products WHERE price < ? and quantity > ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_product_title(conn, product_name):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE %?%'''
        cursor = conn.cursor()
        cursor.execute(sql, (product_name,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


hw_name = 'hw.db'
create_products_table_sql = \
    '''CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
    )'''


connection = create_connection(hw_name)
if connection is not None:
    print("Successfully connected!")
    # create_table(connection, create_products_table_sql)
    # insert_product(connection, ('Wheat bread', 25.0, 3))
    # insert_product(connection, ('Rice', 106.8, 1))
    # insert_product(connection, ('Rye bread', 49.9, 3))
    # insert_product(connection, ('Meat', 600.0, 1))
    # insert_product(connection, ('Flour', 97.7, 2))
    # insert_product(connection, ('Cheese', 455.0, 1))
    # insert_product(connection, ('Milk', 59.9, 1))
    # insert_product(connection, ('Kurut', 53.0, 7))
    # insert_product(connection, ('Cookies', 88.7, 4))
    # insert_product(connection, ('Sweets', 168.3, 2))
    # insert_product(connection, ('Ice-cream', 30.0, 6))
    # insert_product(connection, ('Coca-cola', 141.2, 1))
    # insert_product(connection, ('Paper napkin', 33.0, 8))
    # insert_product(connection, ('Washing powder', 425.4, 1))
    # insert_product(connection, ('Soap', 50.5, 2))
    # update_product_quantity(connection, (6, 9))
    # update_product_price(connection, (112.8, 2))
    # delete_product(connection, 14)
    # select_all_products(connection)
    # select_products_by_price_and_quantity_limit(connection, 100, 5)
    # select_products_by_product_title(connection, 'bread')
    connection.close()
