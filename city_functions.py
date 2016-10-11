# Author: Bojan G. Kalicanin
# Date: 11-Oct-2016
# City, Country: Write a function that accepts two parameters: a city name
# and a country name. The function should return a single string of the form
# City, Country, such as Santiago, Chile. Store the function in a module called
# city_functions.py.
# Create a file called test_cities.py that tests the function you just wrote
# (remember that you need to import unittest and the function you want to test).
# Write a method called test_city_country() to verify that calling your function
# with values such as 'santiago' and 'chile' results in the correct string. Run
# test_cities.py, and make sure test_city_country() passes.

def city_country(city_name, country_name, population=''):
    """
    Function that takes city name and country name and returns a single string
    in the form 'City, Country', like 'Santiago, Chile'.
    """
    if population:
        full_info = city_name.title() + ', ' + country_name.title() + \
            " - population " + str(population)
    else:
        full_info = city_name.title() + ', ' + country_name.title()        
    return full_info