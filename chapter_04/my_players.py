players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Original list of players:")
for player in players:
    print(player)
print(players[-3:])  # Print the last three players in the list
#copying the list
my_players = players[:]
print("\nMy players list (copy of original):")
for player in my_players:
    print(player)