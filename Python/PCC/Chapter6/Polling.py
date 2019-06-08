favorite_langauges = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
ppl = ["ahmad","adam","jen","sarah"]

for i in ppl:
    if i in favorite_langauges.keys():
        print(i+ " thank you for responding to the poll")
    elif i not in favorite_langauges.keys():
        print(i+ " you should take the poll asap")
    else:
        print("You must go to hell")
# for i in favorite_langauges.keys():
# #    print(i)
#     if i in ppl:
#         print(i+ " thank you for responding to the poll")
#     elif i not in ppl:
#         print(i+ " you should tak the poll asap")
#     else:
#         print("Not related to you")
