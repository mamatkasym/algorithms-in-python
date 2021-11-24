from typing import List, Tuple


def three_sum(nums: List[int], target: int) -> Tuple[int, int, int] or int:
    nums = [(v, i) for i, v in enumerate(nums)]
    nums.sort()
    for i in range(len(nums)):
        trg = target - nums[i][0]
        ind = nums[i][1]
        lo = 0
        hi = len(nums) - 1
        result = -1
        while lo != hi:
            if nums[lo][0] + nums[hi][0] == trg:
                result = nums[lo][1], nums[hi][1]
                break
            elif nums[lo][0] + nums[hi][0] < trg:
                lo += 1
            else:
                hi -= 1
        if result != -1:
            a, b = result
            if a != ind and b != ind:
                return i, a, b

    return -1


def test_three_sum():
    import random
    nums = [random.randint(1, 1000) for _ in range(20)]
    exist = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                exist.add(nums[i] + nums[j] + nums[k])

    for x in range(3001):
        if x in exist:
            assert three_sum(nums, x) != -1
        else:
            assert three_sum(nums, x) == -1
