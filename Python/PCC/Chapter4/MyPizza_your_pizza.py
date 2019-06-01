my_pizza = ["Veg","Pepperoni","Classic"]
friends_pizza = my_pizza[:]
for i in my_pizza:
    print("My favorite pizza are: ")
    print(i)
my_pizza.append("Coco")
friends_pizza.append("Zozo")
print("My favorite pizzas are:")
print(my_pizza)
for i in my_pizza:
    print("My favorite pizza are: ")
    print(i)
print("Friends favorite pizzas are:")
print(friends_pizza)
for i in friends_pizza:
    print("Friends favorite pizzas are: ")
    print(i)
