def cheese_and_crackers(cheese_amount , boxes_of_crackers):
    print(f"You have {cheese_amount} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print(f"Man that is enough for the part")
    print("Get a blanket\n")


print("We can just give the functions numbers directly")
cheese_and_crackers(20,30)

print("You can use variables in your script!")
amount_of_cheese = 10
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do even math")
cheese_and_crackers(10*10, 20*20)

print("You can combine the two variables and math")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
