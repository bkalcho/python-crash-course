# Author: Bojan G. Kalicanin
# Date: 07-Oct-2016
# Using json.dump()

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)