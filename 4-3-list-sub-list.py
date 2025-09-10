players = ['charles', 'martina', 'michael', 'florence', 'eli']
# ['charles', 'martina', 'michael']
print(players[0:3])

# ['martina', 'michael', 'florence']
print(players[1:4])

# ['charles', 'martina', 'michael', 'florence']
print(players[:4]) # omit the first index, starts from the beginning

# ['michael', 'florence', 'eli']
print(players[2:]) # omit the last index, goes to the end

# ['michael', 'florence', 'eli']
print(players[-3:]) # the last three players