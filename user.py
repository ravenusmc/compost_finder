#This file will have the class that will create the user object 

class User():

    #Here I describe all the properties that each user object will have
    def __init__(self):
        self.username = ''
        self.email = ''
        self.address = ''
        self.city = ''
        self.state = ''
        self.zipcode = ''
        self.password = ''
        self.coords = 0

    #This method will add the properties to the user object. (Probably could have done this in the init method.)
    def set_up_user(self, username, email, address, city, state, zipcode, password):
        self.username = username
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.password = password