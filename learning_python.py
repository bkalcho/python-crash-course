# Author: Bojan G. Kalicanin
# Date: 05-Oct-2016
# Read from file by reading whole content of the file, by reading file
# line by line in the for loop, and by storing lines in the list

filename = 'learning_python.txt'

# Print the content by reading entire file
with open(filename) as file_object:
    content = file_object.read()
    print(content.rstrip())

# Print content of the file by reading line by line
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Print content of the file by reading line by line and storing
# them into a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())