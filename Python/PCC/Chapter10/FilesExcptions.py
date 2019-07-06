file_path ='pi_digits.txt'

# with open(file_path) as file_object:
#     lines = file_object.readlines()
#     print(lines)
# for line in lines:
#     print(line.rstrip())
#     # for i in file_object:
#     #     print(i.rstrip())
# #        contents = file_object.read()
# #        print(contents.rstrip())

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
