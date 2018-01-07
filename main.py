#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
import json 
import requests

#Importing files that I created for the project
from user import *
from coord import *
from db import *

#Setting up Flask
app = Flask(__name__)

#This route takes the user to the home page
@app.route('/')
def home():
    return render_template('home.html')

#This route take the user to the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Recieving the information from the user.
        username = request.form['username']
        password = request.form['password']
        #creating the db object 
        db = Connection()
        #Checking to see if the user is in the database
        flag, not_found, password_no_match = db.check(username, password)
        #Conditional statement to test if the user is a member of the site.
        if flag == True:
            #If the user is in the database, the user gets sent to the index page.
            session['username'] = request.form['username']
            #Sending the user into the app
            return redirect(url_for('landing'))
        else:
            #If the user is not in the database then they will be sent to the
            #sign up page.
            if not_found:
                flash('Username not found, maybe sign up!')
            elif password_no_match:
                flash('Password does not match! Maybe sign up!')
    return render_template('login.html')

#This route will take the user to the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #Creating a user object 
        user = User()
        #creating the db object
        db = Connection()
        #setting up the coords object
        coords = Coord()
        #Pulling the data that is needed from the form 
        username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zip']
        person_type = request.form['compost']
        password = request.form['password']
        #setting the properties to the user object
        user.set_up_user(username, email, address, city, state, zipcode, person_type, password)
        #Getting the lat and lng coordinates for the user. 
        user = coords.get_coords(user)
        #Encrypting the password
        password, hashed = db.encrypt_pass(user)
        # #Adding the user to the database
        db.insert(user, hashed)
        return redirect(url_for('login'))
    return render_template('signup.html')

#This route will take the user to the landing page-once they sign in
@app.route('/landing')
def landing():
    #This session will prevent users who have not signed up from coming in.
    if 'username' not in session:
        return redirect(url_for('signup'))
    #Pulling the username which I'll use in the database. 
    username = session['username']
    #Creating user object 
    user = User()
    #Creating a connection to the database 
    db = Connection()
    #Pulling the user information out of the database. 
    row = db.pull_user_info(username)
    #Building the user object from the information from the database
    user.build_user(row)
    #With this query I'm pulling all people in the DB who live in a certain area. 
    users = db.find_by_city(user)
    return render_template('landing.html', gardener = row, users = users)

#This route will take the user to a page explaining why one should compost
@app.route('/why')
def why():
    if 'username' not in session:
        return redirect(url_for('signup'))
    return render_template('why.html')

#This function is what will log out the user.
@app.route('/sign_out')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    #Redirect to Landing page
    return redirect(url_for('landing'))

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)