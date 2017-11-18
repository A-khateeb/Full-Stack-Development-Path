import os

totalSize = 0

for filename in os.listdir('C:\\Users\\test\\Dropbox'):
    totalSize = totalSize+os.path.getsize(os.path.join('C:\\Users\\test\\Dropbox',filename))

print(totalSize)

print(os.listdir('C:\\Users\\test\\Dropbox'))