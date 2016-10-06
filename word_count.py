# Author: Bojan G. Kalicanin
# Date: 06-Oct-2016
# Analyze books from input, regarding their number of words

def count_words(filename):
    """Count the approximate number of the words in a file."""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
            " words.")

filenames = [
    'alice.txt',
    'siddhartha.txt',
    'moby_dick.txt',
    'little_women.txt'
    ]

for filename in filenames:
    count_words(filename)