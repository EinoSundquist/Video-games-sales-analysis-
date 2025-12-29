import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user = "root",
    password = "MySQL-S3rver",
    database = "videogame_sales"
)
cursor = mydb.cursor()

#select the top 10 most sold games from na and pal combined.
sql = """
SELECT title, sum(na_sales + pal_sales) AS na_and_pal_sales
FROM sales
GROUP BY title
ORDER BY na_and_pal_sales desc
LIMIT 10
"""

cursor.execute(sql)

myresult = cursor.fetchall()

for row in myresult:
    print(row)


#
sql ="""
SELECT critic_score, sum(total_sales)
FROM sales
WHERE critic_score IS NOT NULL AND total_sales IS NOT NULL
GROUP BY critic_score
ORDER BY sum(total_sales) desc
"""
cursor.execute(sql)
myresult = cursor.fetchall()

critic_scores = []
sales = []

for row in myresult:
    critic_scores.append(row[0])
    sales.append(row[1])

x = np.array(critic_scores)
y = np.array(sales)

coeffs = np.polyfit(x, y, 5)
poly = np.poly1d(coeffs)

#add a sequence of 100 numbers from min to the max critic_score (x)
all_x = np.linspace(x.min(),x.max(), 100)
all_y = poly(all_x)

plt.scatter(x, y, alpha=0.5, label="Data")
plt.plot(all_x, all_y, label="Trend curve")

plt.xlabel("Critic score")
plt.ylabel("Total sales")
plt.title("Correlation of critic scores and total sales")
plt.legend()
plt.show()