import mysql.connector
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user = "root",
    password = "MySQL-S3rver",
    database = "videogame_sales"
)
cursor = mydb.cursor()

sql = """
SELECT * from sales
LIMIT 15
;
"""
cursor.execute(sql)
myresult = cursor.fetchall()

for row in myresult:
    print(row)

sql = """
SELECT publisher, AVG(critic_score)
FROM sales
GROUP BY publisher
ORDER BY AVG(critic_score) desc
LIMIT 15;
"""
cursor.execute(sql)
myresult = cursor.fetchall()
for publisher, critic_score in myresult:
    print(publisher, critic_score)


sql = """
SELECT title, sum(total_sales)
FROM sales
GROUP BY title
ORDER BY sum(total_sales) desc
LIMIT 5;
"""
cursor.execute(sql)
myresult = cursor.fetchall()

title = []
total_sales = []
for row in myresult:
    title.append(row[0])
    total_sales.append(row[1])

#visualize the data
plt.figure(figsize = (15,8))
plt.bar(title, total_sales)
plt.xlabel("Title")
plt.ylabel("Total Sales (mil)")
plt.title("Top 5 most sold video games")
plt.show()