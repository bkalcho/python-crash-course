# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Ask user in restaurant how many people are in their dinner group

group = int(input("How many people will be at your table? "))
if group > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")