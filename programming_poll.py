# Author: Bojan G. Kalicanin
# Date: 06-Oct-2016
# Ask people why they like programming and store their
# responses in a file

filename = 'programming_poll.txt'
message = "Why do you love programming?"
message += "\n(for the end, enter 'quit'): "

while True:
    reason = input(message)

    if reason == 'quit':
        break
    with open(filename, 'a') as file_object:
        file_object.write(reason + "\n")