from random import randrange
s = [1,2,3,4,5,6,7,8,9,10]
'''
for i in range(int(s)):
    i+=1
    c = randrange(i)
    print(c)
'''
#rand_item = s[randrange(len(s))]


rand_items = [s[randrange(len(s))] for s in range(4)]
print(rand_item)
