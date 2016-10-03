# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Build a profile of yourself

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('bojan', 'kalicanin',
                                location='belgrade',
                                faculty='electrical engineering',
                                university='belgrade')
print(user_profile)