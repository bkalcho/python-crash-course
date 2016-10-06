# Author: Bojan G. Kalicanin
# Date: 06-Oct-2016
# Prompt the user for their name, print the greeting on the screen
# and add a line recording their visit

filename = 'guest_book.txt'


with open(filename, 'a') as file_object:
    while True:
        name = input("What is your full name?\n(for end write 'quit'): ")
        if name == 'quit':
            break
        print("Welcome " + name.title() + "!")
        file_object.write(name.title() + " has visited site.\n")