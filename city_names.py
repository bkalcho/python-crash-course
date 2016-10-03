# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Function that takes a city and a country, and prints that information

def city_country(city, country):
    """Return the name of the city and the country
    neatly formatted."""
    message = city + ', ' + country + '!'
    return message.title()

p_message = city_country('belgrade', 'serbia')
print(p_message)

p_message = city_country('new york', 'united states')
print(p_message)

p_message = city_country('jerusalem', 'israel')
print(p_message)