import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table= "Create table users (id int,name text,password text)"
cursor.execute(create_table)
user =(1,'ravali','12345')
users =[(2,'rithwik','5678'),(3,'badari','23456'),(4,'jyothi','12345')]
insert_query="Insert into users values(?,?,?)"
cursor.execute(insert_query,user)
cursor.executemany(insert_query,users)
select_query="Select * from users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
