def printpicnic(itemsdict, left,right):
    print('Picnic Items'.center(left+right, '-'))
    for k,v in itemsdict.items():
        print(k.ljust(left,'.')+str(v).rjust(right))

picnicitem={'Sandwiches':4,'Cups':10,'Apples':17,'Cookies':8000}
printpicnic(picnicitem,12,3)
printpicnic(picnicitem,20,6)

