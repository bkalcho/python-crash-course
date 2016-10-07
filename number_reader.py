# Author: Bojan G. Kalicanin
# Date: 07-Oct-2016
# Program that reads from json file

import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)