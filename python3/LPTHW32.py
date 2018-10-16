the_court = [1,2,3,4,5]
fruits = ["Apples","Oranges","Pears","Apricots"]
change = [1,"Pennies",2,"Dimes",3,"Quarters"]

for number in the_court:
    print(f"The court number is {number}")

for fruit in fruits:
    print(f"The fruit type is: {fruit}")

for i in change:
    print(f"I got {i}")

element = []

for i in range(0,6):
    print(f"Adding element {i} to the list")
    element.append(i)

for i in element:
    print(f"The Element was: {i}")
    
