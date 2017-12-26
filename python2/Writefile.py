import collections

fp = open("hello.txt",'a')
c = fp.write("Hello man")
print(fp)
print(c)
fp = open("hello.txt",'r')
g = fp.read()
print(g)
