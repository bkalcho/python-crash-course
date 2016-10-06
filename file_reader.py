# Author: Bojan G. Kalicanin
# Date: 05-Oct-2016
# Program that reads from a file and prints the content of
# a file to the stdout

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())