# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Make a dictionary of five programming words which is ordered

from collections import OrderedDict
words = OrderedDict()

words['for'] = 'construct for doing repetitive tasks'
words['variable'] = 'a placeholder for some data type'
words['string'] = 'an array of characters'
words['list'] = 'an array of some kind of data type'
words['if'] = 'conditional statement'
words['str()'] = 'function for converting to string'
words['sorted()'] = 'function for temporary sortation of a list'
words['list()'] = 'function for converting to list'

for word, description in words.items():
    print(word.upper() + ":" + "\n\t" + description.title() + ".\n")