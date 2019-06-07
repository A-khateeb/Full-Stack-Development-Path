#Dictionary is a key-value pair
#Color ---> Green, Points ----> 5
# alien_0 = {"color" : "green" , "points" : 5}
#print(alien_0["color"])
#print(alien_0["points"])
#print("You just earned " + str(alien_0["points"]) + " points")
# print(alien_0)
# alien_0['x-position'] = 0
# alien_0['y-position'] = 25
# print(alien_0)
#
# alien_0 = {}
# alien_0['Color'] = 'Green'
# alien_0['Points'] = 5
#
# print("The alien's color is " + alien_0["Color"] +'.')
#
# alien_0["Color"] = 'Yellow'
# print("The alien's color is " + alien_0["Color"] +'.')

# alien_0 ={'x-position' : 0 ,'y-position' : 25, 'speed' : 'fast' }
# print("Original x-position : " + str(alien_0['x-position']))
# if alien_0["speed"] == 'slow':
#     x_increment = 1
# elif alien_0["speed"] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0["x-position"] = alien_0["x-position"] + x_increment
#
# print("New position is : " + str(alien_0['x-position']))
# alien_0 = {"color" : "green" , "points" : 5}
# print(alien_0)
#
# del alien_0["points"]
# print(alien_0)
#

favorite_langauges = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

print("Sarah's favorite langauge is :" +
 str(favorite_langauges['sarah'].title()) +
 '.')
