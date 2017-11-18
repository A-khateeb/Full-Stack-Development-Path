import pprint
import os

cats = [{'name':'Zophie','Desc':'Chubby'},{'name':'Pooka','Desc':'fluffy'}]
pprint.pformat(cats)
fileObj = open('C:\\Users\\test\\Dropbox\\Software Engineer\\Python Code\\Python Code Pprint\\mycats.py','w')
fileObj.write('cats = '+pprint.pformat(cats)+'\n')
fileObj.close()