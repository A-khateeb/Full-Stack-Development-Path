rivers = {"Nile":"egypt","Amazon":"Brazil","River of Jordan":"Jordan & Palestine"}
for river, country in rivers.items():
    print(river.title()+" "+"runs through"+" "+ country.title())


for river in rivers.keys():
    print("The rivers we have are :" + river.title())


for country in rivers.values():
    print("The rivers we have are :" + country.title())
