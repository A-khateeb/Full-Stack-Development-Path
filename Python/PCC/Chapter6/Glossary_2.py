glossary = {"Dictionary":"Is a key-value pair structure",
            "del":"is a method used to delete the list or Dictionary without having any way to retrive data",
            "Lists":"Is an array based structure",
            "Tuple":"Is a list, however, the values cannot change",
            "pop":"is a method used to delete the list or Dictionary without having any way to retrive data"}
for term, meaning in glossary.items():
    print("The meaning of " + term + ":\n" + meaning)
print("""
\n
\n
\n
""")
glossary["Sorted"] = "A function in Dictionary to sort the key/value in order"
glossary["insert"] = "A function in lists to insert to a specific list"
glossary["append"] = "A function in lists to add values to the end of a list"
for term, meaning in glossary.items():
    print("The meaning of " + term + ":\n" + meaning+ "\n")
