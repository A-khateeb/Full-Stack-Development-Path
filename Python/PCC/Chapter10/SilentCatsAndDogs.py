def contents(filename):
    try:
        with open(filename) as fileObject:
            content = fileObject.readlines()
    except FileNotFoundError:
        pass
    else:
        print(content)

filename = ["cats.txt" , "dogss.txt"]
for i in filename:
    contents(i)
