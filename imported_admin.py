# Author: Bojan G. Kalicanin
# Date: 05-Oct-2016
# Working with classes imported from a module

from usersm import Admin

my_user = Admin('john', 'doe', 'jdoe', 30, 'new york')
my_user.privileges.show_privileges()