# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Poll users for their dream vacation

results = {}

while True:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world" +
        " would you go? ")
    
    results[name] = place

    response = input("\nWould you like to allow another user to" +
        "participate in the poll? (yes/no) ")
    if response == 'no':
        break

print("\n--- Poll Results ---")
for name, place in results.items():
    print(name + " would like to visit " + place + ".")