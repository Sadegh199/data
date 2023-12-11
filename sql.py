import mysql.connector

a = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass"
)
b = a.cursor()
sql = "CREATE DATABASE shop"
b.execute(sql)

a = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
  database="shop"
)
b = a.cursor()


def products():
    sql = """
        CREATE TABLE products(
        product_id INT AUTO_INCREMENT,
        product_name VARCHAR(255),
        category_id INT,
       price INT,quantity INT,
        PRIMARY KEY ( product_id),FOREIGN KEY (category_id) REFERENCES categories_table (category_id)
        );
    """
    cursor.execute(sql)
    connection.commit()

def categories():
    
    sql = """
        CREATE TABLE categories(
        category_id INT AUTO_INCREMENT,
        category_name VARCHAR(255),
        PRIMARY KEY ( category_id)
        );
    """
    cursor.execute(sql)
    connection.commit()

def add(product_id, product_name, category_id, price, quantity):
    cursor.execute(f'INSERT INTO products (product_id, product_name, category_id, price, quantity) VALUES ({product_id},{product_name},{category_id, price},{ price},{ quantity})')
    connection.commit()
def add(category_id, category_name):
    cursor.execute(f'INSERT INTO categories (category_id, category_name) VALUES ({category_id}, "{category_name}")')
    connection.commit()    
def remove_t(product_id):
    cursor.execute('DELETE FROM products WHERE product_id = {product_id}')
    connection.commit()   
def remove(category_id):
    cursor.execute(f'DELETE FROM categories WHERE category_id = {category_id}')
    connection.commit()
def edit(product_id, product_name, category_id, price, quantity):
    cursor.execute(f'UPDATE products SET product_name = {product_name}, category_id = {category_id}, price = {price}, quantity = {quantity} WHERE product_id = {product_id}')
    connection.commit()
def edit(category_id, category_name):
    cursor.execute(f'UPDATE categories SET category_name = {category_name} WHERE category_id = {category_id}')
    connection.commit()
def search(product_name):
    cursor.execute(f'SELECT * FROM products WHERE product_name LIKE { product_name}')
    product = cursor.fetchall()
    return product
def search(category_name):
    cursor.execute(f'SELECT * FROM categories WHERE product_name LIKE { category_name}')
    product = cursor.fetchall()
    return product
def show():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for aa in products:
        print(aa)
def shows():
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    for bb in categories:
        print(bb)
