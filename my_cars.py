# Author: Bojan G. Kalicanin
# Date: 04-Oct-2016
# Create instances of Car and ElectricCar in the same module

from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())