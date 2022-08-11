#!/usr/bin/python3
"""
A method for returning change for a given total
"""


def makeChange(coins, total):
    """
    Find the minimum number of coins needed to make change for a given total
    Args:
        coins (list): list of available coins
        total (int): total amount of change to make
    Return:
        int: minimum number of coins needed to make change or -1
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for i in coins:
        if total % i == 0:
            coin_count += int(total / i)
            return coin_count
        if total - i >= 0:
            if int(total / i) > 1:
                coin_count += int(total / i)
                total = total % i
            else:
                coin_count += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count
