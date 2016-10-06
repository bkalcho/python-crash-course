# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Store information about a persons

person_0 = {
    'first_name': 'marko',
    'last_name': 'markovic',
    'age': 25,
    'city': 'belgrade',
    }

person_1 = {
    'first_name': 'nikola',
    'last_name': 'nikolic',
    'age': 28,
    'city': 'novi sad',
    }

person_2 = {
    'first_name': 'john',
    'last_name': 'smith',
    'age': 32,
    'city': 'new york',
    }

people = [person_0, person_1, person_2]

for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    print("\nPerson's name is: " + full_name.title() + ".")
    print("Age: " + str(person['age']))
    print("City: " + person['city'].title())