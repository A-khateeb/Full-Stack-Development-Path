message = 'it was a bright cold day in April, and the clock were striking thirteen'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1


print(count)