# Author: Bojan G. Kalicanin
# Date: 07-Oct-2016
# Greet user whose name has already been stored

import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")