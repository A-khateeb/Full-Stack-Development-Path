def bacon():
    raise Exception('This is an error  message.')

def spam():
    bacon()

spam()
