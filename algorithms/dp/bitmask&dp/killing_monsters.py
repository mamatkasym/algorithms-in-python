"""
You are given an integer array power where power[i] is the power of the ith monster.

You start with 0 mana points, and each day you increase your mana points by gain where gain initially is equal to 1.

Each day, after gaining mana, you can defeat a monster if your mana points are greater than or equal to the power of
that monster. When you defeat a monster:

your mana points will be reset to 0, and
the value of gain increases by 1.
Return the minimum number of days needed to defeat all the monsters
Source: https://leetcode.com/problems/minimum-time-to-kill-all-monsters/
"""
import math


def minimum_time(power: list[int]) -> int:
    n = len(power)
    # dp[i][j] - minimum time to kill i+1 monsters with and the killed monsters in binary representation are
    # for example: dp[1][3] means 2 monsters, that is monster 0 and monster 1 are killed
    dp = [[math.inf] * (1 << n) for _ in range(n)]
    for i in range(n):
        dp[0][1<<i] = power[i]

    for i in range(n-1):
        for j in range(1 << n):
            if dp[i][j] != math.inf:
                for k in range(n):
                    curr = 1 << k
                    if not (j & curr):
                        dp[i+1][j | curr] = min(dp[i+1][j | curr], )