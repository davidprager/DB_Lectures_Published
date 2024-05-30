from flask import Flask, render_template, request, redirect, url_for, make_response
import mysql.connector
import datetime

# instantiate the app
app = Flask(__name__)

# Connect to the database
# todo: Insert code to connect to zoo database

# set up the routes
@app.route('/')
def home():
    # todo: Link to the index page.
    return render_template()

@app.route('/schedule')
def schedule():
    # todo: Get today's date

    # todo: Create dictionary of events

    # todo: Link to the schedule page.  Pass the date as a parameter
    return render_template()

@app.route('/animals')
def animals():
    # todo: Execute query to get the animals from the database

    # todo: Fetch all the rows in a list of tuples called animals.

    # todo: Link to the animals page.  Pass the animals as a parameter
    return render_template()

if __name__ == "__main__":
    app.run(debug = True)
