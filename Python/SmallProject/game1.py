import random
iron = 0
ironS = 0
coal = 0
coalS = 0
diamond = 0
diamondS = 0
lvl = 1
print("Press enter to mine")
while lvl == lvl:
  s = input("")
  if s == "":
    ironS = random.randint(0,lvl*2)
    iron = iron + ironS
    coalS = random.randint(0,lvl*5)
    coal = coal + coalS
    diamondS = random.randint(0,random.randint(0,1*lvl))
    diamond = diamond + diamondS
    print("You have earned",ironS,"iron,",coalS,"coal and",diamondS,"diamond.")
    print("You now have a total of:",iron,"iron,",coal,"coal and",diamond,"diamond.")
    shop = input("Would you like to go to the shop?")
    if "yes" in shop.lower() or shop.lower() == "y" or "shop" in shop.lower():
      upg = input("Would you like to upgrade to the next level?")
      if "yes" in upg.lower() or upg.lower() == "y":
        if coal >= 5*lvl and iron >= 2*lvl and diamond >= 1*lvl:
          lvl = lvl + 1
          iron = 0
          coal = 0
          diamond = 0
          print("You are now at level",lvl)
          print("(press enter to continue)")
        else:
          print("You don't have enough")
          print("(press enter to continue)")
