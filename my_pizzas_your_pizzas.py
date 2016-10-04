# Author: Bojan G. Kalicanin
# Date: 28-Sep-2016
# My pizzas, Your Pizzas

pizzas = ['capricoza', 'vulcano', 'vegetariana', 'quattro stagione']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("I really love pizza!\n")

friend_pizzas = pizzas[:]

pizzas.append('serbiana')
friend_pizzas.append('italiana')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)