file_path  = ("learning_python.txt")
with open(file_path) as file_object:
    content = file_object.read()
    content = content.replace("python" , "C")
    print(content)
