import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "create table if not exists users (id INTEGER Primary key,username text,passwor text)"
item_table ="create table if not exists items(id INTEGER Primary key,name text,price float)"
cursor.execute(create_table)
cursor.execute(item_table)
connection.commit()
connection.close()
