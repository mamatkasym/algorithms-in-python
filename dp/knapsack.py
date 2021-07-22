"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
You cannot break an item, either pick the complete item or don’t pick it (0-1 property)
"""
from typing import List


def knapsack(val: List, weights: List, W: int, N: int):
    """
    Time complexity: O(N*W)
    Memory complexity: O(N*W)
    """
    if not N:
        N = len(weights)
    dp = [[0 for x in range(W + 1)] for x in range(N)]

    for i in range(N):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i] <= w:
                dp[i][w] = max(val[i] + dp[i - 1][w - weights[i]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[N-1][W]


def optimized_space_knapsack(val: List, weights: List, W: int, N: int):
    """
    Time complexity: O(N*W)
    Memory complexity: O(W)
    """
    if not N:
        N = len(weights)
    dp = [0 for x in range(W + 1)]

    for i in range(N):
        for w in range(W, 0, -1):
            if w >= weights[i]:
                dp[w] = max(dp[w], dp[w - weights[i]] + val[i])
    return dp[W]


def fractional_knapsack(val: List, weights: List, W: int, N: int):
    """
    Time complexity: O(N*W)
    Memory complexity: O(W)
    """
    if not N:
        N = len(weights)
    dp = [0 for x in range(W + 1)]
    val = [(w, i) for i, w in enumerate(val)]
    val.sort(key=lambda x: -x[0])
    for v in val:
        for w in range(W, 0, -1):
            if w >= weights[v[1]]:
                dp[w] = max(dp[w], dp[w - weights[v[1]]] + v[0])
            else:
                dp[w] = max(dp[w], dp[0] + v[0] * (w / weights[v[1]]))
    return dp[W]


def test():
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapsack(val, wt, W, n))
    print(optimized_space_knapsack(val, wt, W, n))
    print(fractional_knapsack(val, wt, W, n))


test()
