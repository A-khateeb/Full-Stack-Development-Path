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

def crawel_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_pages_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

print (crawel_web(seed))
