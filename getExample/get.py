from flask import Flask, render_template, request, redirect, url_for, make_response
import mysql.connector
import datetime

# instantiate the app
app = Flask(__name__)

# set up the routes
@app.route('/')
def home():
    numbers = {'1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four'}
    #Link to the first page
    return render_template('pageOne.html', numbers = numbers)

@app.route('/pageTwo')
def pageTwo():
    choice = request.args['choice']
    # Link to second page.  Pass the choice as a parameter
    return render_template('pageTwo.html', choice = choice)

if __name__ == "__main__":
    app.run(debug = True)
