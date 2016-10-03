# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Make a dictonary of cities with their information

cities = {
    'belgrade': {
        'country': 'serbia',
        'population': 2000000,
        'description': 'capital of serbia',
        },
    'london': {
        'country': 'england',
        'population': 8000000,
        'description': 'capital of the uk',
        },
    'new york': {
        'country': 'united states',
        'population': 10000000,
        'description': 'biggest city of the us'
        },
}

for city, info in cities.items():
    print("\nSome facts about the " + city.title() + ":")
    for key, value in info.items():
        if key == 'population':
            print("\t" + key.title() + ": " + str(value))
        else:
            print("\t" + key.title() + ": " + value.title())