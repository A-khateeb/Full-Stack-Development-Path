def product_list(p):
    total = 1
    for e in p:
        total = total*e
    return total



print (product_list([9]))
#>>> 9

print (product_list([1,2,3,4]))
#>>> 24
print (product_list([]))
#>>> 1
