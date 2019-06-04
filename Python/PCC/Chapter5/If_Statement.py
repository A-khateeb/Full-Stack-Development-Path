cars = ["audi","bmw","subaru","toyota"]
for i in cars:
    if i == "audi":
        print(i.upper())
    else:
        print(i.title())

#set the variable i to bmw
i = 'bmw'
#check the equality of the variable (equality operator)
i == 'bmw'

car = "Audi"
print(car.lower() == "Audi")

car = "Audi"
print(car.lower() == "audi")
print(car)

car = "BMW"
car = car.lower() == "bmw"
print(car)

requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies")

age = 18
if age == 18:
    print("True")

answer = 17
if answer != 42:
    print("That was not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

age_0 = 22
age_1 =  18

print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
print((age_0 >= 21) and (age_1 >= 21))
age_0 = 22
age_1 =  18
print(age_0 >=21 or age_1>=21)
age_0 = 18
print((age_0 >=21) or (age_1>=21))
requested_topping = ["mushroom","onions","pineapples"]
print('mushroom' in requested_topping)
print('pepperoni' in requested_topping)


banned_users = ["andrew","carolina","david"]
user = "marie"
if user not in banned_users:
    print(user.title() + " you can post the message you want in the forum")

game_active = True
can_edit = False
