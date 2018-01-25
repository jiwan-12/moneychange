#usr/bin/python
"""
python code to find minimum number of coin required to change money.
"""

"""Function to find the minimum number of coins"""

def money_change(money, coins):
    minimum_coin = [x*0 for x in range(money+1)]
    for m in range(1, money+1):
        minimum_coin[m] = 1000
        for coin in coins:
            if m >= coin:
                if minimum_coin[m-coin]+1 < minimum_coin[m]:
                    minimum_coin[m] = minimum_coin[m-coin]+1
    return minimum_coin

money = 20
coins = [1, 2, 5, 10]
changes = money_change(money, coins)
for m in range(money+1):
    print "Amount=%d Minimum no of coins=%d\n"%(m, changes[m])


