import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="lydia",
    passwd="celeste",
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE lsk")
#my_cursor.execute("DROP DATABASE lsk")
#my_cursor.execute("UPDATE TABLE ")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
