# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Favorite programming languages poll

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

take_poll = ['jen', 'marco', 'phil', 'john']

for person in take_poll:
    if person in favorite_languages.keys():
        print("Thank you "+ person.title() + " for taking a poll!")
    else:
        print(person.title() + ", please take the poll!")