spam = ["Hello", "Hi", "howdy", "heyas"]
while True:

    try:
        print("Please enter the name to search for")
        name = input()
        spam.index(name)
        if name in spam:
            print("The value is correct keep going!")
            print(spam.index(name))
            break
    except :
        if ValueError:
            print("The value is wrong")
            spam.append(name)
            continue

print(spam)

try:
    eggs = "Hello"
    verb = eggs.append("World")
except:
    if AttributeError:
        list(eggs)
        verb = eggs.append("World")
        eggs = eggs["Hello",verb]
        print("We are going to use the List")
        print(eggs)


