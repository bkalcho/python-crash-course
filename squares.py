# Author: Bojan G. Kalicanin
# Date: 27-Sep-2016
# Calculation of square of the first ten squares

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)