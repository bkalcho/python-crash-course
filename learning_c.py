# Author: Bojan G. Kalicanin
# Date: 06-Oct-2016
# Use replace meyhod to replace words.

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'Scala'))