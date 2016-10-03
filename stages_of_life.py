# Author: Bojan G. Kalicanin
# Date: 29-Sep-2016
# Determine person's stage of life

person_age = 23

if person_age < 2:
    person = 'baby'
elif person_age >= 2 and person_age < 4:
    person = 'toddler'
elif person_age >= 4 and person_age < 13:
    person = 'kid'
elif person_age >= 13 and person_age < 20:
    person = 'teenager'
elif person_age >= 20 and person_age < 65:
    person = 'adult'
else:
    person = 'elder'

print(person)