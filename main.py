#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
import json 
import requests

#Setting up Flask
app = Flask(__name__)

#This route takes the user to the landing page
@app.route('/', methods=['GET', 'POST'])
def landing():
    return render_template('login.html')

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)