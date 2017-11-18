while True:

    print("Please type your username")
    name=input()
    if name!='joe':
        continue
    print("Hello Joe")
    print("Please enter your password")
    password=input()
    if password=='swordfish':
        break
    print("Access denied!")
