class Parent(object):
    def implicit(self):
        print("Parent Implicit()")

class Child(Parent):
    pass

dad = Parent()
son =  Child()

dad.implicit()
son.implicit()
