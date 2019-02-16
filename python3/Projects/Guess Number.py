import random

print("I am thinking of a number between 1 and 20")
secretnumber = random.randint(1,20)
for guessnumber in range(1,7):
    print("Take a guess")
    guess=int(input())
    
    if guess < secretnumber:
    print("The number you inserted is too low")
    
    elif guess > secretnumber:
        print("The number you inserted is too high")
    else:
        break

if guess == secretnumber:
        print("That is correct, you figured it out ("+(str(guessnumber))+") number)")
else:
        print("Sorry you could not figure out that the number is "+str(secretnumber))
              
                                                       
