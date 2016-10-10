# Author: Bojan G. Kalicanin
# Date: 10-Oct-2016
# Program that lets users to enter their first and last name, and see a
# neatly formatted full name.

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')