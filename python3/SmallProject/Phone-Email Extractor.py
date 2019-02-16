import re
import pyperclip
from django.contrib.auth.handlers.modwsgi import groups_for_user

regexPhone = re.compile(r'''(
(\d{3}|\(\d{3}\))
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?

)''', re.VERBOSE)

emailRegex = re.compile(r'''
([a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9._+-]+
(\.[A-Za-z]{2,4})
)''',re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in regexPhone.findall(text):
    phonenum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] !='':
        phonenum +='x'+groups[8]
        matches.append(phonenum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("copied to clipboard")
    print('\n'.join(matches))
else:
    print("No phone number or email!")