class Parent(object):
    def implicit(self):
        print("Parent Implicit()")

    def override(self):
        print("Parent Override()")

    def alter(self):
        print("Parent Alter()")


class Child(Parent):
    def override(self):
        print("Child override()")
    def alter(self):
        print("Child before Parent alter ")
        super(Child, self).alter()
        print("Child after Parent Alter")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.alter()
son.alter()
