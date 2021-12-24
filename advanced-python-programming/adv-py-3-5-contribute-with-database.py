import mysql.connector

cnx = mysql.connector.connect(
    user='root', 
    password='',
    host='127.0.0.1',
    database='learn'
    )

query = "SELECT * FROM people;"
cursor.excute(query)



cnx.close()