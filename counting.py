# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Count from 1 to 10 using while loop

current_number = 0
while current_number < 10:
    current_number += 1
    # Print just the odd numbers
    if current_number % 2 == 0:
        continue
    print(current_number)