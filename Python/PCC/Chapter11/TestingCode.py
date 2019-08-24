from functions import get_formated_name

print("Enter q at any time to exit")

while True:
    first = input("Enter your first name: ")
    if first == 'q':
        break
    last = input("Enter your last name: ")
    if last == 'q':
        break

    format_name = get_formated_name(first, last)
    print("\tNeatly formated name : " + format_name + '.')
