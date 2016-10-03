# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Print ordianal numbers

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")        
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")