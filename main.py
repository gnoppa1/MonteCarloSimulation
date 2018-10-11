import random

def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        #print("{}".format(roll))
        return False
    elif roll <= 50:
        #print("{} <= 50".format(roll))
        return False
    elif 50 < roll < 100:
        #print('50 < {} < 100'.format(roll))
        return True

def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        currentWager += 1
    print("Funds: {}".format(value))


###############call
x = 0
while x < 100:
    simple_bettor(10000, 100, 100)
    x += 1