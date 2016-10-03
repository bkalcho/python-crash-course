# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Print each of magician's names from a list

def show_magicians(magicians):
    """Print the names of magicians."""
    for magician in magicians:
        print(magician.title())

magicians_names = ['john', 'mark', 'charly']
show_magicians(magicians_names)