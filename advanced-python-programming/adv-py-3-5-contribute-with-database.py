from typing import Counter
import mysql.connector

cnx = mysql.connector.connect(
    user='root', 
    password='',
    host='127.0.0.1',
    database='learn'
    )

cursor = cnx.cursor()

query = "SELECT * FROM people;"
cursor.execute(query)

for (name, age, sex) in cursor:
    values = f"{name} is a {sex} and the age is {age}."
    print(values)

cnx.close()