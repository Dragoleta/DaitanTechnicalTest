quarters, dimes, nickels, pennies = 25, 10, 5, 1

coins = [quarters, dimes, nickels, pennies]

coinList = []
coinCount = []
naux = 0
n = 12
way = 0




def getNumberOfWays(number, Coins):
 
    ways = [0] * (number + 1);
 
    ways[0] = 1;
 
    for i in range(len(Coins)):
        for j in range(len(ways)):
            if (Coins[i] <= j):
                ways[j] += ways[(int)(j - Coins[i])];
    return ways[number];





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
    coinList.append(coinCount)
    coinCount = []
    naux = 0
    way += 1
    coins.pop(0)