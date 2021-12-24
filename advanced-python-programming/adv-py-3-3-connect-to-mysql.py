import mysql.connector

print("Connecting to db")
cnx = mysql.connector.connect(
    user='root', 
    password='Moh$en1800',
    host='127.0.0.1',
    database='learn'
    )

print("connect to db")

# name = "hassan"
# age = 12
# sex = "u"

# cursor = cnx.cursor()
# cursor.excute(f"INSERT INTO people VALUES ({name}, {age}, {sex})")
# cnx.comit()
cnx.close()