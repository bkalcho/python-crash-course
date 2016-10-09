# Author: Bojan G. Kalicanin
# Date: 09-Oct-2016
# Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a
# separate program that reads in this value and prints the message,
# "I know your favorite number! It’s _____."

import json

filename = 'number.json'

with open(filename) as f_obj:
    number = json.load(f_obj)

print("I know your favorite number! It's " + str(number) + ".")