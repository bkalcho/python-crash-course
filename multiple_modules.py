# Author: Bojan G. Kalicanin
# Date: 05-Oct-2016
# Using class from module, that depends on classes defined in
# another module

from roles import Admin

my_user = Admin('john', 'doe', 'jdoe', 30, 'new york')
my_user.privileges.show_privileges()