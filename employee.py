# Author: Bojan G. Kalicanin
# Date: 11-Oct-2016
#
# Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store
# each of these as attributes. Write a method called give_raise() that
# adds $5000 to the annual salary by default but also accepts a
# different raise amount. Write a test case for Employee. Write two
# test methods, test_give_default_raise() and test_give_custom_raise().
# Use the setUp() method so you don’t have to create a new employee
# instance in each test method. Run your test case, and make sure both
# tests pass.

class Employee():
    """Modeling a real-life employee."""

    def __init__(self, first, last, annual_salary):
        """
        Store employee first name, last name and annual salary as
        class attributes.
        """
        self.first_name = first
        self.last_name = last
        self.annual_salary = annual_salary
        
    def give_raise(self, raise_amount=5000):
        """Method that gives raise to the employee."""
        self.annual_salary += raise_amount