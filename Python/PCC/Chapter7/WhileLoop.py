current_number = 1
while current_number <= 5:
    current_number += 1

print(current_number)
prompt = "Tell me something I will repeat it back to you!"
prompt += "Enter 'quit' to end the program\n"

message = ""
while message != 'quit':
        message = input(prompt)
        if message != 'quit':
            print(message)
while message != 'quit' or message != 'Quit':
    message = input(prompt)
    if message == 'Quit' or message == 'quit':
        print("Quiting the while loop ")
        break
    elif message != 'quit' or message != 'Quit':
        print(message)
    else:
        print("Nothing")

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "Please enter the name of cities you visited\n"
prompt += "(Enter quit when you finish)\n"
#active = True
while True:
    city = input(prompt)
    if city == 'quit':
        print("quitting")
#       active = False
        break
    else:
        print("I'd love to go to " + city.title() + "!" )
current_number = 0
while current_number < 10:
    current_number+=1
    if current_number % 2 == 0:
        continue

    print(current_number)

x = 1
while x <= 5:
    print(x)
    x +=1
