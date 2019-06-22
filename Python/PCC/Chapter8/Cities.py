def Cities(city, country):
    print("\n" + city + " is in " + country + "!")

Cities("Jerusalem","Palestine")
def Cities(city, country = "Palestine"):
    print("\n" + city + " is in " + country + "!")

Cities("Ramallah")
Cities("Haifa")
Cities("Cairo" ,  "Egypt")
