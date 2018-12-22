the_count = [1,2,3,4,5]
fruits = ["Apple","Orange","Pears","Apricots"]
Change = [1,"Pennis",2,"Dims",3,"Quarter"]

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"The fruits type: {fruit}")

for change in Change:
    print(f"I got {change}")

element = []

for i in range(0,6):
    if i == 0 or i == 1:
        print(f"Adding {i} element to the list.")
        element.append(i)
    else:
        print(f"Add {i} elements to the list.")
        element.append(i)

for i in element:
    print(f"The elements are: {i}")
