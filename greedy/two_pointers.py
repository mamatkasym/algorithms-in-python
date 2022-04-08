"""
Given array of numbers and s target numbers. Find two distinct number(distinct position) with their sum equal to target
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int] or int:
    nums.sort()
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        if nums[lo] + nums[hi] == target:
            return lo, hi

        elif nums[lo] + nums[hi] < target:
            lo += 1

        else:
            hi -= 1

    return -1


def test_two_sum():
    import random

    nums = [random.randint(1, 1000) for _ in range(100)]
    exist = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            exist.add(nums[i] + nums[j])
    for x in range(2001):
        if x in exist:
            assert two_sum(nums, x) != -1

        else:
            assert two_sum(nums, x) == -1
