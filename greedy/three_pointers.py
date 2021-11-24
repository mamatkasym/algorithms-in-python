from greedy.two_pointers import two_sum


def three_sum(nums: list[int], target: int) -> tuple[int, int, int] or int:
    nums_wi = [(v, i) for i, v in enumerate(nums)]
    nums.sort()
    for i in range(len(nums)):
        trg = target - nums_wi[i][0]
        result = two_sum(nums, trg)
        if result != -1:
            a, b = result
            if a != i and b != i:
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
