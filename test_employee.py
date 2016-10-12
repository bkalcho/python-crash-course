# Author: Bojan G. Kalicanin
# Date: 11-Oct-2016
# Test case for class Employee from module employee.py

import unittest
from employee import Employee

class TestEmployeeClass(unittest.TestCase):
    """Tests for the class Employee."""
    
    def setUp(self):
        """Create an employee for use in all test methods."""
        self.test_employee = Employee('John', 'Doe', 50000)
        
    def test_give_default_raise(self):
        """
        Test if method give_raise() gives default raise to employee in
        the amount of $5000.
        """
        self.test_employee.give_raise()
        
        self.assertEqual(55000, self.test_employee.annual_salary)
        
    def test_give_custom_raise(self):
        """
        Test if method give_raise() works when custom value, like $13000
        for the raise is provided.
        """
        self.test_employee.give_raise(13000)
        
        self.assertEqual(63000, self.test_employee.annual_salary)
        

unittest.main()