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
        self.lat = 0
        self.lng = 0
        self.person_type = ''

    #This method will add the properties to the user object. (Probably could have done this in the init method.)
    def set_up_user(self, username, email, address, city, state, zipcode, person_type, password):
        self.username = username
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.person_type = person_type
        self.password = password

    #This method will build the user once they are logged in 
    def build_user(self, row):
        self.username = row[1]
        self.email = row[2]
        self.address = row[3]
        self.city = row[4]
        self.state = row[5]
        self.zipcode = row[6]
        self.lat = row[7]
        self.lng = row[8]
        self.person_type = row[9]