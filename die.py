from random import randint

class Die():
    """Trying to model real-world dice with 6 sides."""

    def __init__(self, sides=6):
        """Initialize attributes of the class Die."""
        self.sides = sides

    def roll_die(self):
        """Modeling rolling of the die."""
        num = randint(1, self.sides)
        print("The current number on the die is: " + str(num))