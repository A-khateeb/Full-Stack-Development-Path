a= int(input("INsert the first value"))
b= int(input("INsert the second value"))
#c = max(a,b,key=abs)
def maximum(a,b):
    c = max(a,b,key=abs)
    print(c)
    return a,b
    
maximum(a,b)
