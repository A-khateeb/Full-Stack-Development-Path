import LPTHW44d
class Other(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
#        self.other.override()
        print("Child Override")
    def altered(self):
        print("CHILD Before altered()")
        self.other.altered()
        print("Child after altered()")

son = Child()
parent = Parent()
son.implicit()
son.altered()
son.override()
parent.implicit()
