# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Preventing list of magicians to be changed

def make_great(magicians):
    """Add word Great to each magician."""
    for i in range(len(magicians)):
        magicians[i] = "Great " + magicians[i]
    new_list = []
    for value in magicians:
        new_list.append(value)
    
    return new_list

def show_magicians(magicians):
    """Print the names of magicians."""
    for magician in magicians:
        print(magician.title())

magicians_names = ['john', 'mark', 'charly']
new_list = make_great(magicians_names[:])
print("\nThe new list:")
show_magicians(new_list)
print("\nThe old list:")
show_magicians(magicians_names)