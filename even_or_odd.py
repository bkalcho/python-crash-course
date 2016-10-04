# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Calculates if number is even or odd

number = input("Enter a number, and I'll tell you if it's even or " +
    " odd:")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")