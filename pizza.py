# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Put requested toppings on pizza

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')