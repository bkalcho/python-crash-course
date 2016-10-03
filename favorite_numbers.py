# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Dictionary which contains favorite numbers of persons

favorite_numbers = {
    'milan': [1, 3],
    'milica': [4, 8, 10, 15],
    'nikola': [2],
    'john': [8, 10, 17, 23, 100, 888],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))