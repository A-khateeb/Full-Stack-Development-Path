name=''
while not name:

    print ("What is your name")
    name= input()

print("How many guests will you have")
numofguest=int(input())
if numofguest:
    print("Are you sure you have enough space")

yes=input()
if yes=='yes' or yes=='Yes' or yes=="YES":
        
    print("Perfect")
else:
        print("It is up to you finally")

print("Done")
