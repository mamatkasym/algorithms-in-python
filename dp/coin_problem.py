"""
Given a set
of coin values coins = {c1, c2,..., ck} and a target sum of money n, our task is to
form the sum n using as few coins as possible
"""


def minimum_coins(coins: list[int], target: int) -> int:
    """
    :param coins: set of integer values of coins
    :param target: target number to form
    :return: number of minimum number of coins to form target
    TC: O(len(coins) * target)
    MC: O(len(coins) * target)
    """
    n = len(coins)
    # dp[i] is the minimum number coins required to get a sum i
    dp = [n + 1] * (target + 1)
    # no coins are needed to form empty sum
    dp[0] = 0
    for i in range(target + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i - coin] + 1, dp[i])

    return dp[target]
