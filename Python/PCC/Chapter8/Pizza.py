def make_pizza(size, *toppings):
    print("Making a " + str(size) + "-inch with the following toppings:")
    for topping in toppings:
        print('- '+topping.title())
