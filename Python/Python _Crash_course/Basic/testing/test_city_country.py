import unittest
from city_function import get_city_country

class NameTestCase(unittest.TestCase):
    """ Tests for 'name_function.py'. """
    def test_city_country(self):
        """Do names like 'santiago chile' work?"""
        formatted_name = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')
unittest.main()  