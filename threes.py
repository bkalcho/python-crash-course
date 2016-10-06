# Author: Bojan G. Kalicanin
# Date: 26-Sep-2016
# Print multiples of 3 from 3 to 30

multiples = []
for number in range(1, 31):
    multiple = number * 3
    multiples.append(multiple)

for multiple in multiples:
    print(multiple)