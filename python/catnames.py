catname= []
while True:
    print ("Enter the name of the cats you have"+str(len(catname)+1))
    name = input()
    if name=='':
        break
    catname = catname+[name]
print("The cat names are")
for name in catname:
  print(' '+name)