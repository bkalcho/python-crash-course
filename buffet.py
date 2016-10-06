# Author: Bojan G. Kalicanin
# Date: 28-Sep-2016
# Define a tuple for five simple foods for a buffet-style restaurant

foods = ('eggs and bacon', 'meatballs', 'cereals', 'bread and cheese',
            'bread and smoked ham')

print("At the restaurant we offer next food:")
for food in foods:
    print(food)

#print("""\nProve that item of the tuple can not be modified by trying to \
#assign a new value""")
#foods[1] = 'bread'

foods = ('eggs', 'meatballs', 'bacon', 'bread and cheese',
            'bread and smoked ham')
print("\nNew menu:")
for food in foods:
    print(food)