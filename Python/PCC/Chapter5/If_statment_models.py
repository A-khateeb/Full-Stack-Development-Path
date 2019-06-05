age = 17
if (age >=18 ):
    print("You are old enough to vote!")
    print("Have you registered for voting?")
else:
    print("\nSorry you cannot vote")
    print("Please register when you turn 18")


age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $"+ str(price))


age = 50
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age <65:
    price = 10
else:
    price = 5

print("Your admission cost is $"+ str(price))


requested_topping = ["mushroom","extra cheese"]
if 'mushroom' in requested_topping:
    print("Adding Mushroom")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni")
if 'extra cheese' in requested_topping:
    print("Adding Extra cheese")
print("Finished making your Pizza!")
