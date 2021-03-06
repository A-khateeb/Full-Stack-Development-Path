import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

index = []
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def lookup(index, keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
            break
    return []

def add_pages_to_index(index, url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)

def make_string(p):
    s = ""
    for e in p:
        s = s+e
    return s

def make_big_index(size):
    index = []
    letters = ['a','a','a','a','a','a','a','a']
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) -1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i])+1)
                break
            else:
                letters[i] = 'a'
    return index

#print (make_big_index(3))
#print (make_big_index(100))
#print (make_big_index(10000))
index100000 = make_big_index(100000)


print (index100000)
