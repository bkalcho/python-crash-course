# Author: Bojan G. Kalicanin
# Date: 06-Oct-2016
# Prompt the user for name, and write the name in a file guest.txt

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    file_object.write(first_name.title() + " " + last_name.title())