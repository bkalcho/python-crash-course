# Author: Bojan G. Kalicanin
# Date: 06-Oct-2016
# Write a simple message and store it to the file

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")