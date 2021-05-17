"""
    Subarray with maximum sum with one deletion from it
"""

from typing import List


def maximum_sum(self, arr: List[int]) -> int:
    ans = -10 ** 9
    n = len(arr)

    s = [0] * n  # subarray with maximum sum without deletion ending at position i; 0 <= i < n
    rs = [0] * n  # subarray with maximum sum with deletion ending at position i; 0 <= i < n

    s[0] = rs[0] = arr[0]

    ans = arr[0]

    for i in range(1, n):
        # recursive relations
        s[i] = max(s[i - 1] + arr[i], arr[i])
        rs[i] = max(s[i - 1], rs[i - 1] + arr[i])

        ans = max(ans, rs[i], s[i])

    return ans
