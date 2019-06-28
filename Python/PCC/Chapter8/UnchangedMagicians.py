def make_great(names,last):
    while names:
        current_name = names.pop()
        print("The great " + current_name)
        last.append(current_name)

def mag_names(names):
    for i in names:
        return i

names = ['Adam','Ahmad','Esam']
last = []
make_great(names[:], last)
mag_names(names)
