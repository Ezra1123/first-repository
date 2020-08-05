import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='kbank',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_table():
    
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "CREATE TABLE users (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(30), account_no VARCHAR(12), age INT(3), balance int(30));"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    
    finally:
        connection.close()

    return True

def add_user(name, age, password, acct_no):
    try:
        with connection.cursor() as cursor:
        # Create a new record
            sql = f"INSERT INTO users (name, age, password, account_no) VALUES('{name}',{age}, '{password}', '{acct_no}');"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        
    finally:
        print("successfully Added User..!!")
       

def fetche_user_details(name):
    try:
        with connection.cursor() as cursor:
        # Create a new record
            sql = f"SELECT name, password FROM users WHERE name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data

        
    finally:
        print("successfully fetched..!!")
        connection.close()


def get_balance(name):
    try:
        with connection.cursor() as cursor:
        # Create a new record
            sql = f"SELECT balance FROM users WHERE name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data

        
    finally:
        print("successfully fetched..!!")
        # connection.close()
 
 



def alter_balance(name, balance):
    try:
        with connection.cursor() as cursor:
        # Create a new record
            sql = f"UPDATE users SET balance = {balance} where name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        
    finally:
        print("successfully updated user balance..!!")
        connection.close()

