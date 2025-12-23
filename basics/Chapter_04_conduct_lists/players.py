players = ['charles', 'martina', 'michael', 'florence', 'eli']
r = players[0:3]
print(r) # ['charles', 'martina', 'michael']
print(players[0:3])  # First three players
print(players[1:4])  # Players from index 1 to 3
print(players[:4])   # First four players
print(players[2:])   # Players from index 2 to the end
print(players[-3:])  # Last three players

print("Here are the first three players on my team:")
for player in players[0:3]:
    print(player.title())