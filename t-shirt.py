# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Function tha takes a size and a message that should be printed
# on a shirt

def t_shirt(shirt_size='L', printed_message='I love Python'):
    """Print size of shirt and the message on the shirt"""
    print("\nT-shirt is of size " + shirt_size.upper() + ".")
    print("Message printed on a shirt: " + printed_message.title() + ".")

t_shirt()
t_shirt('m')
t_shirt('xl', printed_message='life is beautiful')