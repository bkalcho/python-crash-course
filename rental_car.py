# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Ask the user what kind of rental car they would like

message = input("Hello, what car you would like to rent? ")
if message.lower() != 'bmw' and message.lower() != 'vw':
    print("Let me see if I can find you a " + message.title() + ".")
else:
    print("Let me see if I can find you a " + message.upper() + ".")