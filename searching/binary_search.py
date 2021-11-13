"""
Suppose that we are given a sorted array of n elements and we want to check if the array contains an element with a target value x
"""
from typing import List


def binary_search1(nums: List[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def binary_search2(nums: List[int], target: int) -> int:
    k = 0
    n = len(nums)
    b = n // 2
    while b >= 1:
        while k + b < n and nums[k+b] <= target:
            k += b
        b //= 2

    if nums[k] == target:
        return k
    return -1


def test():
    nums = [1, 1, 3, 4, 5, 6, 7, 9, 10, 12, 23, 32, 45]
    assert binary_search1(nums, 23) == 10
    assert binary_search1(nums, 11) == -1

    assert binary_search2(nums, 23) == 10
    assert binary_search2(nums, 11) == -1


test()
