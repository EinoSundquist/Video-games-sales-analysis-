import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user = "root",
    password = "MySQL-S3rver",
    database = "videogame_sales"
)
cursor = mydb.cursor()

#modify id column so it begins from 1 instead of 0 so we can make the column auto_increment
"""
sql = "
update sales
set id = id + 1;
"
cursor.execute(sql)
mydb.commit()
"""

#Make the id column auto_increment

sql = """
alter table sales
modify id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;
"""

cursor.execute(sql)
mydb.commit()