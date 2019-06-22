def make_album(artist, title, tracks = ''):
    album = {'artist' : artist , 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
#    print("Insert the name of the artist")
    ar = input("Insert the name of the artist\n")
    if ar == 'q' or ar == 'Q':
        break
    ti = input("Insert the name of the album\n")
    if ti == 'q' or ti == 'Q':
        break
    tr = input("Insert the number of the tracks\n")
    if tr == 'q' or tr == 'Q':
        break

final = make_album(ar, ti, tr)
print(final)
