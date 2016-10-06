# Author: Bojan G. Kalicanin
# Date: 06-Oct-2016
# Program that adds two numbers ant catches TypeError

try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
except ValueError:
    print("You can not perform addition on non numeric values!")
else:
    result = first_number + second_number
    print(str(first_number) + " + " + str(second_number) + " = " +
        str(result))