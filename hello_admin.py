# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Print a greeting to each user

usernames = ['test1', 'test2', 'test3', 'test4', 'admin']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello Admin, would you like to see a status report?")
        else:
            print("Hello " + username.title() + 
                    ", thank you for logging in again.")
else:
    print("We need to find some users!")