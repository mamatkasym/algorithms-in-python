"""
    Kadane's algorithm to find a subarray of array `arr` with maximum sum
    Time complexity: O(len(arr))
"""

from typing import List


def kadane(arr: List[int]) -> int:
    ans = -max(arr) - 1
    s = 0
    for el in arr:
        s = max(s + el, el)
        ans = max(s, ans)

    return ans
