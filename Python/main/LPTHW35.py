from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, lear to type a number!!")
    if how_much < 50:
        print("You are not greedy. You win!!")
    else:
        dead("You greedy basterd!")

def bear_room():
    print("This is a bear here!")
    print("This bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear? ")
    bear_moved = False

    while True:
        choice = input(">")
        if choice == "Take honey!":
            dead("The bear looks at you the slaps your face off!")
        elif choice=="taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg!")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what this means")

def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it, whatever stares at you and you go insane")
    print("Do you flee your life or eat your head? ")
    choice = input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in the dark room!")
    print("There is a door to your right and to your left")
    print("Which one do you take")
    choice = input(">")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve!")

start()
