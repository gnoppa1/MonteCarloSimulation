###################IMPORTS#########################
import random
import matplotlib
import matplotlib.pyplot as plt
import  time

####################SETTINGS###############################
sampleSize = 100
startingFunds = 1000
wagerSize = 100
wagerCount = 1000

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

def doubler_better(funds, initial_wager, wager_count, color):
    value = funds
    wager = initial_wager
    global broke_count

    wX =[]
    vY = []

    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager


    while currentWager <= wager_count:
        if previousWager == 'win':
            #print('Won')
            if rollDice():
                value += wager
                #print(value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                #print(value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    #print('We went broke after {} bets'.format(currentWager))
                    broke_count += 1
                    break
        elif previousWager == 'loss':
            #print('We lost the last one, so we will be smart and double')
            if rollDice():
                wager = previousWagerAmount * 2

                if (value - wager) < 0:
                    wager = value
                #print('We won {}'.format(wager))
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2

                if (value - wager) <= 0:
                    wager = value
                #print('We lost wager {}'.format(wager))
                value -= wager
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    broke_count += 1
                    #print('we went broke after {} bets'.format(currentWager))
                    break
                #print(value)
                previousWager = 'loss'



        currentWager += 1
    #print(value)
    plt.plot(wX, vY, color)

"""xx = 0
broke_count = 0

while xx < 1000:
    doubler_better(10000, 100, 1000)
    xx += 1

death_rate = int(broke_count/float(xx)*100)
survival_rate = int(100 - broke_count/float(xx)*100)

print('Death rate {}'.format(death_rate))
print('Survival rate {}'.format(survival_rate))

plt.axhline(0, color = 'r')
plt.show()"""




def simple_bettor(funds, initial_wager, wager_count, color):
    value = funds
    wager = initial_wager
    global broke_count

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

    if value <= 0:
        broke_count += 1
        value ="broke"

    #print("Funds: {}".format(value))
    plt.plot(wX, vY, color)

###############call
broke_count = 0
x = 0
while x < sampleSize:
    #simple_bettor(startingFunds, wagerSize, wagerCount, 'k')
    doubler_better(startingFunds, wagerSize, wagerCount, 'c')
    x += 1

'''
death_rate = int(broke_count/float(x)*1000)
survival_rate = int(100 - broke_count/float(x)*100)

print('Death rate {}'.format(death_rate))
print('Survival rate {}'.format(survival_rate))
'''

plt.axhline(0, color = 'r')

plt.ylabel('Account value')
plt.xlabel('Wager count')
plt.show()