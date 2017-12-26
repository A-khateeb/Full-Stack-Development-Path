try:
    foo= input("What is the permission you need?")
    fp= open("sample.txt", foo)
    c = fp.read(10)
    fp.close()
    print(c)
except IOError as e:
    print("The file does not exist!", e)
except IndexError as e:
    print("Index out of range!",e)
except ValueError as e:
    print("Insuffient permission!",e)
