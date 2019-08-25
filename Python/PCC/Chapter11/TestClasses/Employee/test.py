from classes import Employee
import unittest

class Test_Employee_class(unittest.TestCase):
    def setUp(self):
        self.eric = Employee("Afeef","khateeb",65000)
    def test_give_raise(self):
        self.eric.give_raise()
        self.assertEqual(self.eric.annual , 70000)
    def test_custom_raise(self):
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.annual , 75000)
unittest.main()
