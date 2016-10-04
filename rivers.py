# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Dictionary of countries and rivers

rivers = {
    'serbia': 'danube',
    'russia': 'volga',
    'brazil': 'amazon',
    'usa': 'mississipi',
    'england': 'thames',
    }

# Print a sentence about each river
for country, river in rivers.items():
    print("The " + river.title() + " runs through " +
        country.title() + ".")
print("\n")

# Print the name of each river included in the dictionary
for river in rivers.values():
    print(river.title())
print("\n")

# Print the name of each country from dictionary
for country in rivers.keys():
    print(country.title())