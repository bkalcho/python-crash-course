# Author: Bojan G. Kalicanin
# Date: 07-Oct-2016
# Program that analyses files from input

def count_word(filename, word):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # Choose to fail silently if information about exception
        # is not important for the user
        pass
    else:
        n_times = contents.lower().count(word)
        print("\nThe word '" + word + "' appears " + str(n_times) +
            " in the file '" + filename + "'!")



w_name = 'the'
filenames = ['alice.txt', 'little_women.txt']
for f_name in filenames:
    count_word(f_name, w_name)