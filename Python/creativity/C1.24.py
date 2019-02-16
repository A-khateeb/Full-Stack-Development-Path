def vowels(a):
    u =  ['A','a','O','o','I','i','E','e','U','u']
    n=0
    for x in a:
        if x in u:
            n+=1
    return n

l= input("Insert some strings!!\n")
print(vowels(l))
