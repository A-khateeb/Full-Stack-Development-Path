from function import Country

print("Insert the city then the country... or insert q to quit")


while True:
    city = input("Please insert the city: ")
    if city == 'q':
        break
    country = input("Please insert the country: ")
    if country == 'q':
        break
    population = input("Please insert the population: ")
    if population == 'q':
        break

    result = Country(city, country, population)
    print(result)
