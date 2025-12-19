import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user = "root",
    password = "MySQL-S3rver",
    database = "videogame_sales"
)
if mydb.is_connected():
    print("Connected to database")