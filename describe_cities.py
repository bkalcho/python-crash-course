# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Function that describes a city

def describe_city(city_name, city_country='usa'):
    """Describe city and country it is in."""
    if city_country.lower() == 'usa':
        print("\n" + city_name.title() + " is in " +
            city_country.upper() + ".") 
    else:
        print("\n" + city_name.title() + " is in " +
            city_country.title() + ".")

describe_city('new york')
describe_city(city_name='los angeles')
describe_city(city_country='serbia', city_name='belgrade')