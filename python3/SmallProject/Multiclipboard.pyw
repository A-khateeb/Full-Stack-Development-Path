#! python3
import os, sys, pyperclip, shelve

myObj = shelve.open('C:\\Users\\test\\Desktop\\mcb.py')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    myObj[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(myObj.keys())))
    elif sys.argv[1] in myObj:
        pyperclip.copy(myObj[sys.argv[1]])

myObj.close()
