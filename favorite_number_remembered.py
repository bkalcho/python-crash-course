# Author: Bojan G. Kalicanin
# Date: 09-Oct-2016
# Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored, report
# the favorite number to the user. If not, prompt for the user’s
# favorite number and store it in a file. Run the program twice to see
# that it works.

import json

filename = 'number_2.json'

try:
    with open(filename) as f_obj:
        number = json.load(f_obj)

except FileNotFoundError:
    number = int(input("What's your favorite number? "))
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)

else:
    print("I know your favorite number! It's " + str(number) + ".")