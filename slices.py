# Author: Bojan G. Kalicanin
# Date: 28-Sep-2016
# Working with a slice of the list

cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

print("The first three items in the list are:")
print(cubes[:3])

print("Three items from the middle of the list are:")
print(cubes[4:7])

print("The last three items in the list are:")
print(cubes[-3:])