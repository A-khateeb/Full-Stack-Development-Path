import json
def get_username():
    filename = 'user.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_user():
    username = input("What is your name? ")
    filename = 'user.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
def greet_user():
    username = get_username()
    if username:
        print("Welcome back " + username)
    else:
        get_new_user()
        print("We will remember your username next time " + str(username))
greet_user()
