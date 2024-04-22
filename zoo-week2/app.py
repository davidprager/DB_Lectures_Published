from flask import Flask, render_template, request, redirect, url_for, make_response
import mysql.connector
import datetime
import os

# instantiate the app
app = Flask(__name__)

# Connect to the database
# Insert code to connect to zoo database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "dap123",
    database = "zoo"
)
cursor = mydb.cursor()

# set up the routes
@app.route('/')
def home():
    # Link to the index page.
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    # Get today's date
    d = datetime.datetime.now()
    date_string = f'{d.month}/{d.day}/{d.year}'
    # Create dictionary of events
    events = {"10:00": "Zoo opens", "12:00" : "Lunch Time", "15:00": "Zoo closes"}
    # Link to the schedule page.  Pass the date as a parameter
    return render_template('schedule.html', date = date_string, schedule = events
                           )

@app.route('/animals')
def animals():
    # Execute query to get the animals from the database
    query = "select animalType, animalSize, animalColor from animal"
    cursor.execute(query)

    # Fetch all the rows in a list of tuples called animals.
    animals = cursor.fetchall()
    # Link to the animals page.  Pass the animals as a parameter
    return render_template('animals.html', animals = animals)

@app.route('/newAnimal')
def newAnimal():
    # Execute query to get the animal sizes from the database
    query = "SELECT DISTINCT animalSize from animal"
    cursor.execute(query)

    # Fetch all the rows in a list of tuples called animals.
    sizes = cursor.fetchall()

    # Link to the newAnimal page.
    return render_template('newAnimal.html', sizes = sizes)

# set up route to process form
@app.route('/newAnimal', methods=['POST'])
def insertAnimal():
    # Retrieve data from form
    type = request.form['animalType']
    size = request.form['animalSize']
    color = request.form['animalColor']

    # insert the new animal into the database
    query = "INSERT INTO animal (animalType, animalSize, animalColor) VALUES (%s, %s, %s)"
    record = (type, size, color)
    cursor.execute(query, record)
    mydb.commit()

    # save image file to images folder
    file = request.files['animalImage']
    filename = type + ".png"
    file.save("static/images/" + filename)

    # Redirect to the animals.html page
    return redirect(url_for ('animals'))

if __name__ == "__main__":
    app.run(debug = True)
