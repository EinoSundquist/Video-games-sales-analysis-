import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user = "root",
    password = "MySQL-S3rver",
    database = "videogame_sales"
)
cursor = mydb.cursor()

sql = """
insert into sales  (title, console, genre, publisher, developer, critic_score, total_sales)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
values = [
    ("Wii sports", "Wii","Sports" ,"Nintendo","Nintendo", 8.1, 82.9),
    ("Minecraft", "X360", "Adventure", "4J Studios", "Microsoft Studios", 8.3, 22)
]

for value in values:
    cursor.execute(sql, value)

mydb.commit()

sql = """
select * from sales
where title = "Wii sports"
"""

cursor.execute(sql)
myresult = cursor.fetchall()

print(myresult)