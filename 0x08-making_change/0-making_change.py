#!/usr/bin/python3
"""makeChange module"""


def makeChange(coins, total):
    """
    determines the fewest number of coins needed to meet a given amount total,
    given a pile of coins of different values
    Arguments:
        coins (int): list of values of coins
        total (int): total amount in question
    Return: fewest number of coins required to meet `total`
    """
    if total < 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1  # The total amount cannot be met by any number of coins
    else:
        return dp[total]

