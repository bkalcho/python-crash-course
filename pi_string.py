# Author: Bojan G. Kalicanin
# Date: 05-Oct-2016
# Program that builds a single string containing all the digits in the
# file with no whitespace in it.

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))