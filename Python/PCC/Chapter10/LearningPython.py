file_path = ("learning_python.txt")
with open(file_path) as file_object:
    lines = file_object.read()
    print(lines)
with open(file_path) as file_object:
    for i in file_object:
        print(i)
with open(file_path) as file_object:
    lines = file_object.readlines()
    for i in lines:
        print(i)
