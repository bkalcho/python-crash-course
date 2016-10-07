# Author: Bojan G. Kalicanin
# Date: 07-Oct-2016
# Program that reads two files and handles FileNotFoundError

def print_files_content(*filenames):
    """
    Function which takes an arbitrary number of files as arguments, and
    then prints the content of each file from the list of passed
    arguments. Function handles FileNotFoundError in the controlled way.
    """
    
    for filename in filenames:
        try:
            with open(filename) as f_obj:
                lines = f_obj.readlines()
        except FileNotFoundError:
            # Next pass statement ensures that except
            # block fails silently.
            pass
            # Comment previous line, and uncomment next line, to give
            # indication when exception occurs.
            # print("\nThe file " + filename + " has not been found!")
        else:
            print("\nThe content of the " + filename + " is:")
            for line in lines:
                print(line.rstrip())


print_files_content('cats.txt', 'dogs.txt')