def make_sandwich(*additions):
    print("Making the sandwich with the following additions")
    for a in additions:
        print("- "+ a.title())

make_sandwich("Cheese")
make_sandwich('Salami','Cheese','tomato')
make_sandwich('Salami','bread','Cheese','tomato','Cucumber')
