responses = {}
questions = True
while questions:
    question1 = input("What is your name? ")
    response = input("What part of world you want to visit ? ")
    responses[question1] = response
    repeat = input("Would you like other person to respond? (Yes/No) ")
    if repeat == 'No' or repeat == 'no':
        questions = False

for name, response in responses.items():
    print(name + " would like to visit " + response)
        
