# glossary = {"Dictionary":"Is a key-value pair structure",
#             "del":"is a method used to delete the list or Dictionary without having any way to retrive data",
#             "Lists":"Is an array based structure",
#             "Tuple":"Is a list, however, the values cannot change",
#             "pop":"is a method used to delete the list or Dictionary without having any way to retrive data"}
# for term, meaning in glossary.items():
#     print("The meaning of " + term + ":\n" + meaning)
# print("""
# \n
# \n
# \n
# """)

from collections import OrderedDict

glossary = OrderedDict()

glossary["Dictionary"] = "Is a key-value pair structure"
glossary["del"] = "is a method used to delete the list or Dictionary without having any way to retrive data"
glossary["Lists"] = "Is an array based structure"
glossary["Tuple"] = "Is a list, however, the values cannot change"
glossary["pop"] = "is a method used to delete the list or Dictionary without having any way to retrive data"

for name, meaning in glossary.items():
    print(name.title() + ": "+ meaning )
