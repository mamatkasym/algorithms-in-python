"""
Given array of numbers and s target numbers. Find two distinct number(distinct position) with their sum equal to target
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
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

    return -1, -1


def test_two_sum():
    import random
    nums = [random.randint(1, 1000) for _ in range(100)]
    target = random.randint(1, 1000)
    a, b = two_sum(nums, target)
    if (a, b) != (-1, -1):
        assert nums[a] + nums[b] == target

    nums = [2, 3, 5, 1, 4, 4, 9, 4, 3, 8]
    assert two_sum(nums, 10) != (-1, -1)
    assert two_sum(nums, 15) == (-1, -1)
    assert two_sum(nums, 8) != (-1, -1)
    assert two_sum(nums, 2) == (-1, -1)
