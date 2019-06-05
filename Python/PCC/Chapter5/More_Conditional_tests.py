name = "afeef"

print("Is the name == afeef" + " I predict it is False\n")
print(name.title() == 'afeef')

print("\nIs the name == Afeef" + " I predict it is True\n")
print(name.title() == 'Afeef')

number = 19
print("\nIs the number =  20 " + " I predict it is true\n")
print(number == 19)


print("\nIs the number =  20 " + " I predict it is true\n")
print(number <= 19)


print("\nIs the number =  20 " + " I predict it is False\n")
print(number < 19)


print("\nIs the number =  20 " + " I predict it is False\n")
print(number > 19)

print("\nIs the number =  20 " + " I predict it is True\n")
print(number >= 19)

number_1 = 10
number_2 = 20

print("\nIs number 1 and number 2 evaluate to True" + " I predict it is true\n")
print(number_1 <=10 and number_2 ==20)

print("\nIs number 1 or number 2 evaluate to True" + " I predict it is true\n")
print(number_1 <=10 or number_2 ==20)


computers = ["apple","dell","samsumg","asus","lenovo"]
print("\nIs Apple in the list " +" I think it is \n")
check = "apple"
print(check.lower() in computers)
value = "sony"
if value not in computers:
    print("\n"+value.title()+ " not in the list\n ")
    computers.append(value)
    print("\n"+value.title() + " added to the list\n")
    print(computers)


users = ["ahmad","ali","afeef"]
print('Afeef'.lower() in users)
print('afeef'.upper() not in users)

users_added = True
