def make_album(artist, title, tracks = ''):
    album = {'artist' : artist , 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

l = make_album("Ahmad",'Tough','26')
print(l)
l = make_album("Jack",'LLL')
print(l)
l = make_album("Ahmad",'Tough',100)
print(l)
