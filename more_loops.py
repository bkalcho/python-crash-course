# Author: Bojan G. Kalicanin
# Date: 28-Sep-2016
# Use for loops to print each list of foods

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)