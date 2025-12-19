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
select * from sales
limit 15
;
"""
cursor.execute(sql)
myresult = cursor.fetchall()

for row in myresult:
    print(row)

sql = """
select publisher, AVG(critic_score)
from sales
group by publisher
order by AVG(critic_score) desc
limit 15;
"""
cursor.execute(sql)
myresult = cursor.fetchall()
for publisher, critic_score in myresult:
    print(publisher, critic_score)


sql = """
select title, sum(total_sales)
from sales
group by title
order by sum(total_sales) desc
limit 5;
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