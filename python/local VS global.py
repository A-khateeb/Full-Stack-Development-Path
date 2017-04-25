def spam():
    global eggs #Global
    eggs="spam"

def bacon():
    eggs = "bacon" #Local

def ham():
    print(eggs) #Global 

eggs = 42   #Global 
spam()
print(eggs)
