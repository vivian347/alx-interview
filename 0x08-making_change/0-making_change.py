#!/usr/bin/python3

"""0-making_change.py
"""


def makeChange(coins, total):
    """determine fewest number of coins to meet a given total
    """
    coins.sort(reverse=True)
    totalCoins = 0

    if total <= 0:
        return 0

    for coin in coins:
        while coin <= total:
            totalCoins += 1
            total -= coin

    if total > 0:
        return -1
    else:
        return totalCoins
