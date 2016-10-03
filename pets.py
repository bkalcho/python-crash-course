# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Pets, displays pet's name and animal kind

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')