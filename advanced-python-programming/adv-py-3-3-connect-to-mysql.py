import mysql.connector

print("Connecting to db")
cnx = mysql.connector.connect(
    user='root', 
    password='',
    host='127.0.0.1',
    database='learn'
    )

print("connect to db")

name = "hassan"
age = 12
sex = "u"

cursor = cnx.cursor()
# cursor.execute(f"INSERT INTO people VALUES ('hasan', 12, 'u')")
cursor.execute(f"INSERT INTO people VALUES ('{name}', {age}, '{sex}')")
cnx.commit()

cnx.close()