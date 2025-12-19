import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user = "root",
    password = "MySQL-S3rver",
    database = "videogame_sales"
)
cursor = mydb.cursor()

sql = """
DELETE FROM sales WHERE title = "Wii sports";
"""

cursor.execute(sql)

sql = """
DELETE FROM sales WHERE title = "Minecraft" and console = "X360";
"""
cursor.execute(sql)

mydb.commit()