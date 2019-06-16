active = True
age = 0
while active:
    age = int(input("Please insert your age\n"))
    if age == "quit":
        break
    else:
        if age < 3:
            print("The ticket is free!")
        elif age >= 3 and age <= 12:
            print("Ticket price is $10")
        else:
            print("Ticket price is $15")
