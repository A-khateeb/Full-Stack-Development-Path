from collections import OrderedDict
fav_lang = OrderedDict()
fav_lang["jen"] = 'python'
fav_lang["sarah"] = 'c'
fav_lang["edward"] = 'ruby'
fav_lang["phil"] = 'python'

for name, prog_lang in fav_lang.items():
    print(name.title() + "'s favorite langauge is " + prog_lang.title())
    
