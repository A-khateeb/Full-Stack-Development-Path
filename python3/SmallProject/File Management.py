import os


baconfile = open('C:\\Users\\test\\Desktop\\hello world','w')
baconfile.write('Hello World!')
baconfile.close()
baconfile = open('C:\\Users\\test\\Desktop\\hello world','a')
baconfile.write("Bacon is not vegetable!")
baconfile.close()
baconfile = open("C:\\Users\\test\\Desktop\\hello world")
content = baconfile.read()
print(content)
