# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Ask a user for desired pizza topping until they enter quit

prompt = "\nPlease tell me a topping you would like to put " + \
    "on your pizza"
prompt += "\nFor end of the input enter 'quit': "

while True:
    topping = input(prompt)

    if topping != 'quit':
        print(topping.title() + "'ll be added to your pizza!")
    else:
        break