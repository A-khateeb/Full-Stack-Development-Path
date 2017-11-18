def get_page(url):
    try:
        if url == "http://xkcd.com/353":
            return  '<html><body>I cant get enough <a href="http://www.udacity.com/cs101x/index.html">crawling</a>!</body></html>'
        elif url == "http://xkcd.com/554":
            return  '<html><body>This is a test page for learning to crawl!<p>It is a good idea to <a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a>before you try to <a href="http://www.udacity.com/cs101x/walking.html">walk</a> or <a href="http://www.udacity.com/cs101x/flying.html">fly</a>.</p></body></html>'
    except:
        return ""
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"',start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    toCrawl = [seed]
    crawled = []
    while toCrawl:
        page = toCrawl.pop()
        if page not in crawled:
            union(toCrawl,get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

page = get_page("http://xkcd.com/554")
print (crawl_web(page))
