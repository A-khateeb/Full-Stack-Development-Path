def eggs(someParameters):
    someParameters.append("Hello")

spam = [1,2,3]
eggs(spam)
print(spam)
print(hex(id(eggs)))
print(hex(id(spam)))
print(eggs)