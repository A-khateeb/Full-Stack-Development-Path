names = []
if names:
    for i in names:
        if i == "admin":
            print("Hello admin, we have users")
        else:
            print("Hello " + i)
else:
    print("no users in the list")
