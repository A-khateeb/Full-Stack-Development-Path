#Access Elements using Index
#Append
#Insertion using specific Indexis
#Remove elements using index
#Remove elements without any backup
#Remove elements with any backup
#Remove by value
#sort
#Sorted
#Reverse order
#Length
locations = ["Istanbul", "Amman", "Amsterdam","London","San Fransisco"]
elements = locations[0]
print(elements)
elements = locations[1]
print(elements)
elements = locations[2]
print(elements)
elements = locations[3]
print(elements)
elements = locations[4]
print(elements)
locations.append("Jerusalem")
print("Appending Locations list"+ str(locations))
locations.insert(1,"Bali")
print(locations)
locations.insert(-1,"Damascus")
print(locations)
locations.pop(5)
print(locations)
Remove_Item = locations.remove("Amman")
print(locations)
removedLocations = locations.pop(0)
print("Removed Locations = "+ str(removedLocations))
print("Locations = "+ str(locations))
print("Using Sorted!")
Sort_Location = sorted(locations)
print(Sort_Location)
print(locations)
print("Using Sort")
print(locations.sort())
print(locations)
print("Using Reverse!")
locations.reverse()
print(locations)
print(locations.sort())
print("The length of the list is "+ str(len(locations)))
print("Deleting the list")
del locations
print(locations)
