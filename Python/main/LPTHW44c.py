class Parent1(object):
    def altered1(self):
        print("Parent1 Altered()")

class Child1(Parent1):
    def altered1(self):
        print("Child Altered()")
        super(Child1, self).altered1()
        print("Child1 After")


class Parent(object):
    def altered(self):
        print("Parent altered()")

class Child(Parent, Child1):
    def altered(self):
        print("Child before Parent alter")
        super(Child, self).altered()
        print("Child after parent alter()")
        super(Child1, self).altered1()
        print("Child1 after parent alter()")

dad = Parent()
son =  Child()

dad.altered()
son.altered()
