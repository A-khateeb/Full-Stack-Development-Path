import unittest
from function import Country

class TestResult(unittest.TestCase):
    def test_City_country(self):
        res = Country('jerusalem', 'palestine')
        self.assertEqual(res, 'Jerusalem, Palestine')
    def test_City_Country_Population(self):
        res = Country('jerusalem','palestine','5000000')
        self.assertEqual(res, 'Jerusalem, Palestine -Population: 5000000')

unittest.main()
