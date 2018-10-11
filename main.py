###################required imports#########################
import random
import matplotlib
import matplotlib.pyplot as plt
import  time



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

def doubler_better(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX =[]
    vY = []

    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager


    while currentWager <= wager_count:
        if previousWager == 'win':
            print('Won')
            if rollDice():
                value += wager
                print(value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                print(value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    print('We went broke after {} bets'.format(currentWager))
                    break
        elif previousWager == 'loss':
            print('We lost the last one, so we will be smart and double')
            if rollDice():
                wager = previousWagerAmount * 2
                print('We won {}'.format(wager))
                value += wager
                print(value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                print('We lost wager {}'.format(wager))
                value -= wager
                if value < 0:
                    print('we went broke after {} bets'.format(currentWager))
                    break
                print(value)
                previousWager = 'loss'

                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

        currentWager += 1
    print(value)
    plt.plot(wX, vY)

doubler_better(10000, 100, 100)
plt.show()

time.sleep(555)



def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX =[]
    vY = []

    currentWager = 1

    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

        currentWager += 1

    if value < 0:
        value ="broke"

    #print("Funds: {}".format(value))
    plt.plot(wX, vY)

###############call
x = 0
while x < 100:
    simple_bettor(10000, 100, 1000)
    x += 1

plt.ylabel('Account value')
plt.xlabel('Wager count')
plt.show()