# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Print all information about car
# Function demonstrate mixing positional and arbitrary keyword arguments

def make_car(manufacturer, model_name, **other):
    """Print information about car."""
    cars = {}
    cars['manufact'] = manufacturer
    cars['model'] = model_name
    for key, value in other.items():
        cars[key] = value
    return cars

car_info = make_car('mercedes', 'a180', origin='germany', segment='b')
print(car_info)