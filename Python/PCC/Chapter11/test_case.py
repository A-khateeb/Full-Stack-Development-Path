import unittest
from functions import get_formated_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formated_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_middle_last_name(self):
        formated_name = get_formated_name('wolfgng', 'amadeus', 'mozart')
        self.assertEqual(formated_name, 'Wolfgng Mozart Amadeus')
    def test_first_integer_last_name(self):
        formated_name = get_formated_name('wolfgng', 1, 'mozart')
        self.assertEqual(formated_name, 'Wolfgng Mozart Amadeus')
unittest.main()
