index = []
def add_to_index(index, keyword, url):
    index.append([keyword, url])

def lookup(index, keyword):
    result = []
    for entry in index:
        if entry[0] == keyword:
            result.append(entry[1])
    return result
