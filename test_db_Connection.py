import mysql.connector
# 1. create connection
# 2. create pointer to db
# 3. command execute, read result
# 4. connection close

connection = mysql.connector.connect(
    host='localhost',
    user="root",
    password="xxxx",
    database="corona_db"
)
# A cursor acts as a pointer or iterator to the records returned by a SELECT statement,enabling you to fetch and process
# data row by row. Cursors are commonly used in database programming when you need to interact with a database
# programmatically. The cursor acts as an interface between your Python code and the database, allowing you to execute
# SQL queries and fetch the results.
cursor = connection.cursor()

# Example: Execute a SELECT query
cursor.execute("SELECT * FROM USER")

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
connection.close()
