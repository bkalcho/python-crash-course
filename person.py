# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Build a person

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimy', 'hendrix', age=27)
print(musician)

musician = build_person('john', 'hooker')
print(musician)