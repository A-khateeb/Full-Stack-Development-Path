players = ["Adam","Charles","Martin","Florence","Michael"]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[:5])
print(players[0:])
print(players[2:])
print(len(players))
print(players[-3:])

print("Here are the first three players of the team:")
for players in players[:3]:
    print(players)
