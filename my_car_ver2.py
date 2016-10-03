# Author: Bojan G. Kalicanin
# Date: 03-Oct-2016
# Import Car class from a module car

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()