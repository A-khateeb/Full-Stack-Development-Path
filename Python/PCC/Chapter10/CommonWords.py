filepath = "Alice.txt"
try:
    with open(filepath) as fileObject:
        content = fileObject.read()
except FileNotFoundError:
    pass
else:
    words = content.split()
    count_words = words.count('the')
    print(count_words)
