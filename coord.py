#This class will convert the address to latitude and longitude coordinates.

#importing outside libraries for use in this project
import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyDU9r9IHb-CSuo2nXSTZWsRugAAQFZIfwA')

class Coord():

    #This function gets the lat and long coordinates based on the user address. This method will 
    #then also take those coordinates and add them to the user object. 
    def get_coords(self, user):
        #Setting a variable to get the full address
        full_address = user.address + ', ' + user.city + ', ' + user.state
        #Placing the full address into the geocode method
        geocode_result = gmaps.geocode(full_address)
        #Getting the exact coordinates from all the information that is returned from the method.
        coordinates = geocode_result[0]['geometry']['location']
        #Here I am setting the lat and long coordinates to individual properties on the user object
        user.lat = coordinates["lat"]
        user.lng = coordinates["lng"]
        #Returning the modified user object. 
        return user
        

    
