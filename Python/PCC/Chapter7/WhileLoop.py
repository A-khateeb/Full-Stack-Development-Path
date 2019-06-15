# current_number = 1
# while current_number <= 5:
#     current_number += 1
#
# print(current_number)
# prompt = "Tell me something I will repeat it back to you!"
# prompt += "Enter 'quit' to end the program\n"
#
# # message = ""
# # # while message != 'quit':
# # #         message = input(prompt)
# # #         if message != 'quit':
# # #             print(message)
# # while message != 'quit' or message != 'Quit':
# #     message = input(prompt)
# #     if message == 'Quit' or message == 'quit':
# #         print("Quiting the while loop ")
# #         break
# #     elif message != 'quit' or message != 'Quit':
# #         print(message)
# #     else:
# #         print("Nothing")
#
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#
prompt = "Please enter the name of cities you visited\n"
prompt += "(Enter quit when you finish)\n"
while True:
    city = input(prompt)
    if city == 'quit':
        print("quitting")
        break
    else:
        print("I'd love to go to " + city.title() + "!" )
