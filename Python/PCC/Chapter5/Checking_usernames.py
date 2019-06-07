current_users = ["Ahmad","Ali","Muhammad","Mustafa","Afeef","Mahmoud","admin"]
new_users = ["Ahmad","Abdallah","Muhammad","Mustafa","Afeef","Malek","Ihab"]

for i in new_users:
    if i not in current_users:
        print("The username is available " + i)
    else:
        print("The username is already taken! " + i )
