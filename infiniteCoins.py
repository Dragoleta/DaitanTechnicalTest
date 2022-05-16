from os import remove


quarters, dimes, nickels, pennies = 25, 10, 5, 1



# gets the amount of possible ways of calculating the change
def getNumberOfWays(number, Coins):
 
    ways = [0] * (number + 1);
    ways[0] = 1;
 
    for i in range(len(Coins)):
        for j in range(len(ways)):
            if (Coins[i] <= j):
                ways[j] += ways[(int)(j - Coins[i])];
    return ways[number];


# Mantains the list with 4 digits
def mantaim4( coinCount):
    while len(coinCount) < 4:
        coinCount.insert(0, 0)
    return coinCount
   
# MakeChanges:
# recieves a set value
# iterates all the coins and add its value to a counter
# makes and return a list of 4 of the possible changes
# 

def makeChanges(n):

    coins = [quarters, dimes, nickels, pennies]
    coinList = []
    coinCount = []
    naux = 0
    way = 0
    ways = getNumberOfWays( n,coins)
    
    while way < ways:
        for coin in coins:
            count = 0
            while naux < n:
                naux += coin
                if naux > n:
                    naux -= coin
                    break    
                count += 1
            coinCount.append(count)    
        coinCount = mantaim4(coinCount)
        if coinCount not in coinList:
            coinList.append(coinCount)
        
        coinCount = []
        naux = 0
        way += 1
        try:
            coins.pop(0)
        except:
            coinList.pop()
            print(coinList)
            return coinList

makeChanges(100)