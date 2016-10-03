# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Print the list of the great magicians

def make_great(magicians):
    """Add word Great to each magician."""
    for i in range(len(magicians)):
        magicians[i] = "Great " + magicians[i]

def show_magicians(magicians):
    """Print the names of magicians."""
    for magician in magicians:
        print(magician.title())

magicians_names = ['john', 'mark', 'charly']
make_great(magicians_names)
show_magicians(magicians_names)