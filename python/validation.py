'''
while True:
    print("Enter your age")
    age=input()
    if age.isdecimal():
        break

    print("Enter a valid number")
'''
while True:
    print("Please enter a password (letter and numbers)")
    password = input()
    if password.isalnum():
        break
    print("Enter a password to protect you!")