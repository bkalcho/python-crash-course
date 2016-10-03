# Author: Bojan G. Kalicanin
# Date: 02-Oct-2016
# Creating class to model a Restaurant, and instantiation of the class
# Calling methods and attributes of the object (class instance)

class Restaurant():
    """Trying to model real world restaurant."""

    def __init__(self, restaurant_name, cousine_type):
        """Initialize restaurant_name and causine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Method that describes restaurant."""
        print("The " + self.restaurant_name.title() + " offers " +
                self.cousine_type + " cousine to the guests.")
    
    def open_restaurant(self):
        """Method thad models opening of the restaurant."""
        print("The " +  self.restaurant_name.title() +
                " is open.")

    def set_number_served(self, number_served):
        """Method that sets number of customers you have served."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increment the number of served customers."""
        self.number_served += number_served

restaurant = Restaurant('hazienda','mexican')
favorite_restaurant = Restaurant('casa nova', 'french')
ethno_restaurant = Restaurant('zavicaj', 'serbian ethnic causine')

restaurant.restaurant_name
restaurant.cousine_type
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 150
restaurant.set_number_served(35)
restaurant.increment_number_served(35)
print("Number of served customers: " + str(restaurant.number_served))

favorite_restaurant.describe_restaurant()
ethno_restaurant.describe_restaurant()