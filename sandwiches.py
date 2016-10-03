# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Program that prints summary of the sandwich that is being ordered
# Program demonstrates usage of arbitrary number of arguments

def sendwich_addings(*addings):
    """Print the summary of the sendwich."""
    print("\nSendwich with next items has been ordered:")
    for adding in addings:
        print("- " + adding)

sendwich_addings('eggs')
sendwich_addings('bacon', 'eggs', 'mayonese')
sendwich_addings('tuna', 'cheese', 'onion', 'ketchup')