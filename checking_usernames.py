# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Check if username is unique

current_users = ['test1', 'test2', 'test3', 'test4', 'test5']

new_users = ['test1', 'ad1', 'ad2', 'test3', 'test5']

for user in new_users:
    if user in current_users:
        if user.lower() == 'test1':
            print("Enter new username")
        else:
            print("Username is available")
