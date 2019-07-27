import json
# numbers = [2,3,5,7,11,13]
# filename = "numbers.json"
# with open(filename , 'w') as file_object:
#     json.dump(numbers, file_object)

username = input("What is your name?")

filename = 'username.json'
with open(filename , 'w') as file_object:
    json.dump(username , file_object)
    print("We will remember your username next time " + username + '!')
