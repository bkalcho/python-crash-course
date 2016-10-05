# Author: Bojan G. Kalicanin
# Date: 05-Oct-2016
# Storing lines from a file in a list, which we can use outside
# the with statement block

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())