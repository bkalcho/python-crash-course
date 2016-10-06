# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Make a list of sendwich orders and make a list of finished sendwiches
# As each sendwich from the list of sendwich order is made move it to 
# finished sendwiches list

sendwich_orders = [
    'tuna sendwich',
    'fish sendwich',
    'cuccumber sendwich',
    'bacon sendwich',
    ]
finished_sendwiches = []

while sendwich_orders:
    sendwich = sendwich_orders.pop()
    finished_sendwiches.append(sendwich)
    print("I made your " + sendwich)

print("\nThe list of all sendwiches that has been made: ")
print(finished_sendwiches)