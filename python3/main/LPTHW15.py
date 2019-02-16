#Imports ARGV from sys
from sys import argv
#Created two arguments an assign them to argv
script, filename = argv
#Opens the text file (filename) and assign it to txt
txt = open(filename)
print(f"Here is your file {filename}")
#Reads the file and prints the content of the file to output
print(txt.read())
print("Type the filename again")
#Prompts the user to insert the file path/name to the code
file_again = input("--> ")
#Opens the text file (filename) and assign it to txt
txt_again = open(file_again)
#Reads the file and prints the content of the file to output
print(txt_again.read())
txt_again.close()
