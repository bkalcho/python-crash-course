# Author: Bojan G. Kalicanin
# Date: 06-Oct-2016
# Appending content to a file

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also like fining mining in large datasets.\n")
    file_object.write("I love creating apps that can run in a" +
        " browser.\n")