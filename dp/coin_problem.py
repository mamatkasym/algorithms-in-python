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
    # first coin used to construct optimal solution
    first = [0] * (target + 1)
    # no coins are needed to form empty sum
    dp[0] = 0
    for i in range(target + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i] < dp[i - coin] + 1:
                dp[i] = dp[i - coin] + 1
                first[i] = coin

# ******** Optional logs *************************************
    print(f'Optimal solution construct {target} is:')
    while target - first[target] > 0:
        print(first[target], '+', end=' ')
        target -= first[target]
    print('=', len(first) - 1)
# *************************************************************

    return dp[target]
