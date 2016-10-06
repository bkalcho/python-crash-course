"""Restaurant class which models real-world restaurant."""

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