# Author: Bojan G. Kalicanin
# Date: 03-Oct-2016
# Model Ice Cream stand a specific kind of the restaurant

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


class IceCreamStand(Restaurant):
    """
    IceCreamStand restaurant class, which models real-world Ice Cream 
    Stand restaurant.
    """

    def __init__(
        self,
        restaurant_name,
        cousine_type='ice creams'):
        """
        Initialize parent class attributes and add IceCreamStand
        specific attributes.
        """
        super().__init__(restaurant_name, cousine_type)
        self.flavors = [
            'strawberry',
            'vanila',
            'malaga',
            'chocolate',
            'blackberry',
            'annanas',
            ]

    def display_flavors(self):
        """Method that displays list of flavors."""
        print("The restaurant " + self.restaurant_name.title() +
            " can offer next ice cream flavors:")
        for flavor in self.flavors:
            print("- " + flavor)


ice_car = IceCreamStand('dolly')
ice_car.display_flavors()