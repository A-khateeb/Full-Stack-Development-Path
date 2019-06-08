# alien_0 ={'Color':'Green','Point':5}
# alien_1 ={'Color':'Yellow','Point':10}
# alien_2 ={'Color':'Red','Point':15}
#
# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
#     for i,m in alien.items():
#         print(str(i) +  " "+ str(m))
#

# aliens = []
# for alien_number in range(30):
#     new_alien = {'color':'green','points':5,'speed':'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[0:6]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'medium'
# for alien in aliens[11:17]:
#     if alien['color'] == 'green':
#         alien['color'] = 'red'
#         alien['points'] = 15
#         alien['speed'] = 'fast'
# for i in aliens[:5]:
#     print(i)
# print(".....")
# print("Total number of aliens is " + str(len(aliens)))
#
#
# pizza = {
# 'crust' : 'thick',
# 'topping' : ['mushroom','extra cheese'],
# }
# print ("You ordered " + pizza['crust'] + 'topping' + " with the following topping")
# for topping in pizza['topping']:
#     print("\t" + topping)
# favorite_langauges = {
#     'jen':['python','ruby'],
#     'sarah':['c'],
#     'edward':['ruby','go'],
#     'phil':['python','haskell'],
# }
# for name, language in favorite_langauges.items():
#     if len(language) > 1:
#         print("\n" + name.title() + "'s favorite langauge are:")
#     else:
#         print("\n" + name.title() + "'s favorite langauge is:")
#     for i in language:
#         print(i.title())



users = {
'aeinstein' :{
'First':'albert',
'last':'aeinstein',
'location':'princeton'
},
'mcurie' :{
'First':'marie',
'last':'curie',
'location':'paris'
},
}

for username, user_infor in users.items():
    print("\nUsername:" + username.title())
    full_name = user_infor['First'] + " " + user_infor['last']
    location = user_infor['location']
    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())
