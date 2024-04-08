"""
This program inserts a record into a database
"""

import mysql.connector

# Create connection object
mydb= mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "dap123",
    database= "class"
)

# Create cursor
cursor = mydb.cursor()

# Define query
query = ("INSERT INTO class (name, age, gender, height, weight) VALUES (%s, %s, %s, %s, %s)")

# Define record
record = ("David", 29, "M", 68, 155)

# Execute query
cursor.execute(query, record)
mydb.commit()
print (cursor.rowcount, "record inserted.")