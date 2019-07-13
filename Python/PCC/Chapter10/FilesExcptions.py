# file_path ='pi_digits.txt'
#
# # with open(file_path) as file_object:
# #     lines = file_object.readlines()
# #     print(lines)
# # for line in lines:
# #     print(line.rstrip())
# #     # for i in file_object:
# #     #     print(i.rstrip())
# # #        contents = file_object.read()
# # #        print(contents.rstrip())
#
# # with open(file_path) as file_object:
# #     lines = file_object.readlines()
# #
# # pi_string = ''
# # for line in lines:
# #     pi_string += line.rstrip()
# # print(pi_string)
# # print(len(pi_string))
#
# # with open(file_path) as file_object:
# #     for a in file_object:
# #         print(a.rstrip())
#
# with open(file_path) as file_object:
#     lines = file_object.readlines()
#
# # print(lines)
# # for line in lines:
# #     print(line.rstrip())
#
# pi_string = ''
#
# for line in lines:
#     pi_string += line.strip()
#
# birthday = input("Enter your birthday in a format mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday is in the first million digit of pi")
#     print(birthday)
# else:
#     print("Your birthday does not appear in the pi digits")
# print(pi_string[:52] + ".....")
# print(len(pi_string))
file_path = ("programming.txt")
with open(file_path, 'w') as file_object:
    file_object.write("I love programming \n")
    file_object.write("I love programming and sport ")

file_path = ("programming2.txt")
with open(file_path, 'a') as file_object:
#    file_object.write("I love programming \n")
#    file_object.write("I love programming and sport ")
#    file_object.write("I love building games ")
    file_object.write("\nI love eating water mellon ")
