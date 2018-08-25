import requests
r = requests.get('https://api.github.com/user', auth=('A-khateeb', 'palasc19912011'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
