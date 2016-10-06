# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Make informations about favorite places

favorite_places = {
    'nikola': ['sidney', 'new york'],
    'john': ['jerusalem'],
    'milan': ['belgrade', 'novi sad', 'london'],
    }

for key, value in favorite_places.items():
    if len(value) > 1:
        print("\n" + key.title() + "'s favorite places are: ")
        for place in value:
            print(place.title())
    else:
        print("\n" + key.title() + "'s favorite place is:")
        for place in value:
            print(place.title())