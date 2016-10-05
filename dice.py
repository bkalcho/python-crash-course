# Author: Bojan G. Kalicanin
# Date: 05-Oct-2016
# Simulate rolling of dices with different number of sides

from die import Die

print("\nRolling the 6 sides Die... ")
six_side_die = Die()
for i in range(10):
    six_side_die.roll_die()

print("\nRolling the 10 sides Die... ")
ten_side_die = Die(10)
for i in range(10):
    ten_side_die.roll_die()

print("\nRolling the 20 sides Die... ")
twenty_side_die = Die(20)
for i in range(10):
    twenty_side_die.roll_die()