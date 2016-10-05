# Author: Bojan G. Kalicanin
# Date: 05-Oct-2016
# Program that reads file line by line and prints line by line
# on the stdout

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())