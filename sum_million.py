# Author: Bojan G. Kalicanin
# Date: 28-Sep-2016
# Sum first million of numbers. Also determine min and max of the list of the
# first million numbers, to make sure that list begins with one and ends
# with one million

numbers = list(range(1, 1000001))

print("Minimum element of the list is: " + str(min(numbers)))
print("Maximum element of the list is: " +  str(max(numbers)))
print("Sum of the list is: " +  str(sum(numbers)))