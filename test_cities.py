# Author: Bojan G. Kalicanin
# Date: 11-Oct-2016
# Test functions from the module city_functions.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do city, country names like 'Santiago, Chile' work?"""
        full_string = city_country('Santiago', 'Chile')
        self.assertEqual(full_string, 'Santiago, Chile')
        
    def test_city_country_population(self):
        """
        Do city, country names with population like
        'Santiago, Chile - population 5000000' work?
        """
        full_string = city_country('Los Angeles', 'California', 8000000)
        self.assertEqual(
            full_string,
            'Los Angeles, California - population 8000000')


unittest.main()