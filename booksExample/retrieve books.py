'''
This program gets books from the book database
'''

import mysql.connector

# Connect to books database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dap123",
    database = "books"
)
# Set up cursor
cursor = mydb.cursor()

user_category = input("What kind of books would you like? ")

# Create query
query = "SELECT title FROM book WHERE category LIKE %s"

# Execute query
cursor.execute(query, ("%" + user_category + "%",))

# Retrieve all the books into a list of tuples
books = cursor.fetchall()
# Display message if no books found
if len(books) == 0:
    print (f"We don't have any {user_category} books")
else:
    # Print all the books
    for row in books:
        print (row[0])


