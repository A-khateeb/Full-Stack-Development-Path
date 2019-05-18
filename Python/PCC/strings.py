#Change case
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#Concatination
first_name = "afeef"
last_name = "khateeb"
full_name = first_name.title() + " " + last_name
print("Hello "+ full_name+ "!")

#Add whitespace with Tab or newline
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavacript")
print("Languages:\n\tPython\n\tC\n\tJavacript")

#Stripping whitespace
favorite_langauge = "Python "
print(favorite_langauge.rsplit())
favorite_langauge = " Python "
print(favorite_langauge.lstrip())
favorite_langauge = favorite_langauge.strip()
print(favorite_langauge)
