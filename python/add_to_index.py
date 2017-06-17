index = []
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print (index)

def lookup(index, keyword):
    for e in index: 
        if e[0] == keyword:
            return e[1]
            break
    return []

print (lookup(index,'udacity'))
print (lookup(index,'hello'))

def add_pages_to_index(index, url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)

add_pages_to_index(index,'fake.text',"This is a test")
add_pages_to_index(index, 'not.test',"This is not a test")
print (index)
