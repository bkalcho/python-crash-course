# Author: Bojan G. Kalicanin
# Date: 02-Oct-2016
# Definition of the Dog class.
# Dog will have next properties: name, age
# Dog will have next methods: sit, roll_over

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")\

    def roll_over(self):
        """Simulate dog roll over in response to a command."""
        print(self.name.title() + " rolled over!")

# Instantiation of the Class Dog.
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")