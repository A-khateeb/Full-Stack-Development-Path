def get_page(url):
	try:
	    import urllib
	    return urllib.urlopen(url).read()

	except:
	    return "error"

words = get_page('https://www.facebook.com')
print (words)
