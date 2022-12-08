strat = []
with open("input.txt", "r") as f:
    for line in f:
        strat.append(line.strip('\n').split(' '))

points = 0

# Part 1
'''
for game in strat:
    diff = ord(game[1]) - ord(game[0])
    if diff == 23:
        points += 3 + ord(game[1]) - 87
    else:
        if game[0] == 'A' and game[1] == 'Z':
            points += ord(game[1]) - 87
        elif game[0] == 'C' and game[1] == 'X':
            points += 6 + ord(game[1]) - 87
        elif diff > 23:
            points += 6 + ord(game[1]) - 87
        else:
            points += ord(game[1]) - 87
'''

for game in strat:
    if game[1] == 'Y':
        points += 3+ ord(game[0]) - 64
    elif game[1] == 'X':
        if game[0] == 'A':
            points += ord('C') - 64
        elif game[0] == 'B':
            points += ord('A') - 64
        else:
            points += ord('B') - 64
    else:
        if game[0] == 'A':
            points += ord('B') - 64
        elif game[0] == 'B':
            points += ord('C') - 64
        else:
            points += ord('A') - 64
        points += 6
        

print(points)