# Author: Bojan G. Kalicanin
# Date: 28-Sep-2016
# Print all car's names in titlecase except for BMW. BMW should be
# written all in uppercase.

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())