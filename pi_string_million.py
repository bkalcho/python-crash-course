# Author: Bojan G. Kalicanin
# Date: 05-Oct-2016
# Read a file of pi in one million decimal spaces

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))