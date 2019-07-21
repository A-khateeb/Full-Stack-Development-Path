def contents(filename):
    try:
        with open(filename) as fileObject:
            content = fileObject.readlines()
    except FileNotFoundError:
        message = "File " + filename + "cannot be found"
        print(messgae)
    else:
        print(content)

filename = ["cats.txt" , "dogs.txt"]
for i in filename:
    contents(i)
