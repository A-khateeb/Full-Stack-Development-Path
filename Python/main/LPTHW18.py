def print_two(*argv):
    argv1 , argv2 = argv
    print(f"Argument one: {argv1}, Argument two: {argv2}")

def print_two_again(argv1, argv2):
    print(f"Argument one: {argv1}, Argument two: {argv2}")

def print_one(argv):
    print(f"Argument one: {argv}")

def print_none():
    print("I got nothing")

print_two("Zed","Show")
print_two_again("Zed", "Show")
print_one("First")
print_none()
