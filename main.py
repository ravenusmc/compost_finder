#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
import json 
import requests

#Importing files that I created for the project
from user import *
from coord import *

#Setting up Flask
app = Flask(__name__)

#This route takes the user to the landing page
@app.route('/')
def landing():
    return render_template('home.html')

#This route take the user to the login page
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #Creating a user object 
        user = User()
        #Pulling the data that is needed from the form 
        username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zip']
        password = request.form['password']
        #setting the properties to the user object
        user.set_up_user(username, email, address, city, state, zipcode, password)
        #setting up the coords object
        coords = Coord()
        #Getting the lat and lng coordinates for the user. 
        user = coords.get_coords(user)

    return render_template('signup.html')


# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)