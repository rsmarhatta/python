import random
numberOfStreaks = 0

CHANCE = ['H','T']
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flip = []
    for i in range(100):

        coin_flip.append(random.choice(CHANCE))

    #Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(coin_flip)-6):

        if coin_flip[i:i+6].count('H') == 6 or coin_flip[i:i+6].count('T') == 6:
            numberOfStreaks += 1
            break
    #print(coin_flip)
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

