from flask import Flask, render_template, request, redirect, url_for, make_response
import mysql.connector
import datetime

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
    # todo: Execute query to get the animals from the database

    # todo: Fetch all the rows in a list of tuples called animals.

    # todo: Link to the animals page.  Pass the animals as a parameter
    return render_template()

if __name__ == "__main__":
    app.run(debug = True)
