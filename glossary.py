# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Make a dictionary of five programming words

words = {
    'for': 'construct for doing repetitive tasks',
    'variable': 'a placeholder for some data type',
    'string': 'an array of characters',
    'list': 'an array of some kind of data type',
    'if': 'conditional statement',
    'str()': 'function for converting to string',
    'sorted()': 'function for temporary sortation of a list',
    'list()': 'function for converting to list',
    }

for word, description in words.items():
    print(word.upper() + ":" + "\n\t" + description.title() + ".\n")