import json

filename = 'numbers.json'
with open(filename) as fileObject:
    numbers = json.load(fileObject)

print(numbers)
