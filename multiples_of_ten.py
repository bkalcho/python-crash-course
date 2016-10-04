# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Ask the user for a number, and then report whether
# the number is a multiple of 10 or not

number = int(input("Tell me a number? "))
if number % 10 == 0:
    print("Your number is multiple of the number 10!")
else:
    print("Your number is not multiple of the number 10!")