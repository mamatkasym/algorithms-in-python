"""
Suppose that we are given a sorted array of n elements, and we want to check if the array contains an element with
a target value x
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
        while k + b < n and nums[k + b] <= target:
            k += b
        b //= 2

    if nums[k] == target:
        return k
    return -1


def lower_bound(nums: list[int], target: int) -> int:
    """
    returns index of the first smallest element in the list bigger than or equal to target,
    or -1 if there is no such element.
    Similar built-in function: bisect.bisect_left
    """
    if not nums:
        return -1
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l if l < len(nums) else -1

def lower_bound(nums: list[int], target: int) -> int:
    pass


def binary_search_template(arr: list):
    def condition(value) -> bool:
        pass

    def _lower_bound():
        pass

    def _upper_bound():
        pass

        left, right = _lower_bound(), _upper_bound()  # could be [0, n], [1, n] etc. Depends on problem
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left

def minimum_satisfying_condition(low: int, high: int, condition: callable):
    while low < high:
        mid = low + (high - low) // 2
        if condition(mid):
            high = mid
        else:
            low = mid + 1
    return low

def test():
    nums = [1, 1, 3, 4, 5, 6, 7, 9, 10, 12, 23, 32, 45]
    assert binary_search1(nums, 23) == 10
    assert binary_search1(nums, 11) == -1

    assert binary_search2(nums, 23) == 10
    assert binary_search2(nums, 11) == -1
