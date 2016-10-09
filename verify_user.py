# Author: Bojan G. Kalicanin
# Date: 09-Oct-2016
# Verify User: The final listing for remember_me.py assumes either that
# the user has already entered their username or that the program is
# running for the first time. We should modify it in case the current
# user is not the person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user
# if this is the correct username. If it’s not, call get_new_username()
# to get the correct username.

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    filename = 'username.json'
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def query_user(username):
    """Query user if it's his/hers name."""
    answer = input("Is your username: '" + username + "'?(yes/no) ")
    if answer.lower() == 'yes':
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username +
            "!")


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    
    if username:
        query_user(username)
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username +
            "!")

greet_user()