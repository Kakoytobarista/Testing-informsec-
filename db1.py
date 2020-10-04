import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='my_db'
)
cursor = conn.cursor()
# # conn.close()
# cursor.execute("use world;")
# cursor.execute("SELECT continent, SUM(population) FROM country GROUP BY 1 HAVING SUM(population) > 400000000;")
# results = cursor.fetchall()
# print(results)
