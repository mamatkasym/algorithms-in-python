"""
Source: https://leetcode.com/problems/candy/
"""
import math


def candy(ratings: list[int]) -> int:
    # Bound two sides with big number
    ratings = [math.inf] + ratings + [math.inf]
    n = len(ratings)
    # ans[i] is the number of candies child `i` gets where 1 <= i <= n-1
    ans = [0] * n
    for i in range(1, n-1):
        # Skip this case as we calculate it later
        if ratings[i-1] > ratings[i] > ratings[i+1]:
            continue
        if ratings[i] > ratings[i-1]:
            # gets more candies than its neighbor
            ans[i] = ans[i-1] + 1
        else:
            left = i
            curr = 1
            # Calculate all skipped in first case
            while left > 0 and ratings[left] < ratings[left-1]:
                ans[left] = curr
                curr += 1
                left -= 1
            # Update ans[left]
            ans[left] = max(ans[left], curr)
    # Exclude two endpoints
    return sum(ans[1:-1])


def candy_alternative(ratings: list[int]) -> int:
    n, ans = len(ratings), [1] * len(ratings)

    for i in range(n - 1):
        if ratings[i] < ratings[i + 1]:
            ans[i + 1] = max(1 + ans[i], ans[i + 1])

    for i in range(n - 2, -1, -1):
        if ratings[i + 1] < ratings[i]:
            ans[i] = max(1 + ans[i + 1], ans[i])

    return sum(ans)
