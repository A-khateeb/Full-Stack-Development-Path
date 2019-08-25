"""
A class to accept first and last name with default or custom salary
"""
class Employee():
    def __init__(self, fname, lname, annual):
        self.fname= fname
        self.lname = lname
        self.annual = annual
    def give_raise(self, amount= 5000):
        self.annual +=amount
        return self.annual
