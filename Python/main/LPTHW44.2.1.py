class Parent():
    pass

class Child(Parent):
    def __init__(self , stuff):
        self.stuff = stuff
        super(Child, self).__init__()
