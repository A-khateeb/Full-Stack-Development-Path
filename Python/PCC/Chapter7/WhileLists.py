unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    print("loading...")
    confirmed_users.append(current_user)

print("\n")
print("The following users have been confirmed!\n")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


############################################################################################
###################                                                 ########################
############################################################################################

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']

print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)

############################################################################################
###################                                                 ########################
############################################################################################
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    response = input("What mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to take the poll again? (Yes/No)")
    if repeat == 'no' or repeat == 'No':
        polling_active = False

print("\n-------Polling Results-------\n")
for name, response in responses.items():
    print(name + " would like to climb "+ response.title())
