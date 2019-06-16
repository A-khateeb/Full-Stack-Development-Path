#toppings = ""
while True:
    prompt = input("Please insert the topping you want to add\n")
    if prompt == 'quit' or prompt == 'Quit':
        break
    else:
        print("Adding " + prompt.title())
