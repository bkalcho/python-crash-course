# Author: Bojan G. Kalicanin
# Date: 28-Sep-2016
# Make a list of the first 10 cubes

cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)