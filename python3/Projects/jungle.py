def jungle_animal(animal, my_speed):
    if animal == 'Zebra':
        print("Try to rid a Zebra")

    elif animal == 'Cheetah':
        if(my_speed>115):
            print('Run')
        else:
            print("Stay Calm and Wait")

    else:
        print("Introduce yourself!")


jungle_animal('Cheetah',1)
jungle_animal('Cheetah',1123)
jungle_animal('Gorila',1)
jungle_animal('Zebra',1)