# Author: Bojan G. Kalicanin
# Date: 30-Sep-2016
# Simple greeter function

def get_formatted_name(first_name, last_name):
    """Display formatted full name."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# This is an infinite loop
while True:
    print("\nTell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")