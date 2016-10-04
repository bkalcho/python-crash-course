# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Create a fleet of 30 aliens

aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))