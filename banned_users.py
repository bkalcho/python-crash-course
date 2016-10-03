# Author: Bojan G. Kalicanin
# Date: 28-Sep-2016
# Print a message to the user if he is not banned

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post response if you wish.")