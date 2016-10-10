# Author: Bojan G. Kalicanin
# Date: 10-Oct-2016
# Function that returns neatly formatted full name.

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()