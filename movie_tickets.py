# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Movie tickets prices

prompt = "\nEnter your age, and I'll tell you the price of the ticket."
prompt += "\nEnter the 'quit' if you want to exit: "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)    
    if age < 3:
        print("Ticket is free.")
    elif age >= 3 and age <= 12:
        print("Ticket price is $10.")
    elif age > 12:
        print("Ticket price is $15.")