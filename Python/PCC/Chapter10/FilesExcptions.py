file_path ='pi_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()
    print(lines)
for line in lines:
    print(line.rstrip())
    for i in file_object:
        print(i.rstrip())
        contents = file_object.read()
        print(contents.rstrip())

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

with open(file_path) as file_object:
    for a in file_object:
        print(a.rstrip())

with open(file_path) as file_object:
    lines = file_object.readlines()

print(lines)
for line in lines:
    print(line.rstrip())

pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday in a format mmddyy: ")
if birthday in pi_string:
    print("Your birthday is in the first million digit of pi")
    print(birthday)
else:
    print("Your birthday does not appear in the pi digits")
print(pi_string[:52] + ".....")
print(len(pi_string))
file_path = ("programming.txt")
with open(file_path, 'w') as file_object:
    file_object.write("I love programming \n")
    file_object.write("I love programming and sport ")

file_path = ("programming2.txt")
with open(file_path, 'a') as file_object:
   file_object.write("I love programming \n")
   file_object.write("I love programming and sport ")
   file_object.write("I love building games ")
   file_object.write("\nI love eating water mellon ")

try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by Zero")

print("Give me two numbers and I will divide them for you")
print("Insert Q/q to quit")
while True:
    first_number = input("Insert the first number: ")
    if first_number == 'q' or first_number == 'Q':
        break
    second_number = input("Insert the second number: ")
    if second_number == 'q' or second_number== 'Q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by Zero")
    else:
        print(answer)
filepath = 'location.txt'
try:
    with open(filepath) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = 'Sorry, the filer ' + filepath + ' does not exist'
    print(message)

title = "Alice in Wonderland"
a = title.split()
print(a)

filename = 'Alice.txt'
try:
    with open(filename) as file_object:
        content = file_object.read()
except FileNotFoundError:
    mesg = 'Sorry, we could not find ' + filename
    print(mesg)
else:
    count = content.split()
    count_words = len(count)
    print("The file " + filename + ' contains about ' + str(count_words) + ' words' )
def count_words(filename):
    try:
        with open(filename, encoding="utf8") as file_object:
            content = file_object.read()
    except FileNotFoundError:
        # message = 'Sorry, the file ' + filename + ' does not exist'
        # print(message)
        pass
    except UnicodeDecodeError:
        print("could not decode file" + filename)
    except FileExistsError:
        pass
    else:
        count = content.split()
        count_words = len(count)
        print("The file " + filename + ' has about ' + str(count_words) + ' words')

filename = ['Alice.txt', 'film1.txt','film12.txt','film3.txt']
for i in filename:
    count_words(i)
