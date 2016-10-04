# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Make a list of sendwich orders and make a list of finished sendwiches
# As each sendwich from the list of sendwich order is made move it to 
# finished sendwiches list

sendwich_orders = [
    'pastrami sendwich',
    'tuna sendwich',
    'fish sendwich',
    'pastrami sendwich',
    'cuccumber sendwich',
    'bacon sendwich',
    'pastrami sendwich',
    ]
finished_sendwiches = []

print("\nDeli has run out of pastrami!")
while 'pastrami sendwich' in sendwich_orders:
    sendwich_orders.remove('pastrami sendwich')

while sendwich_orders:
    sendwich = sendwich_orders.pop()
    finished_sendwiches.append(sendwich)
    print("I made your " + sendwich)

if 'pastrami sendwich' not in finished_sendwiches:
    print("\nPastrami sendwich is not in finished orders.")
else:
    print("\nPastrami sendwich is in the list of finished orders.")

print("\nThe list of all sendwiches that has been made: ")
print(finished_sendwiches)