import random


def subarray_minimums_sum(arr: list[int]) -> int:
    """
    https://leetcode.com/problems/sum-of-subarray-minimums
    Returns sum of minimums of all subarrays of arr
    """
    # stack keeps index of last found minimum element
    stack = [-1]
    n = len(arr)
    answer = 0
    for i in range(n):
        while len(stack) > 1 and arr[stack[-1]] >= arr[i]:
            last = stack.pop()
            answer += (i - last) * (last - stack[-1]) * arr[last]
        stack.append(i)

    while len(stack) > 1:
        last = stack.pop()
        answer += (n - last) * (last - stack[-1]) * arr[last]

    return answer


# -------- TESTS --------------------------------------------------

def test_subarray_minimums_sum():
    N = random.randint(10, 100)
    arr = [random.randint(1, 100) for _ in range(N)]
    sm = 0
    for i in range(N):
        for j in range(i+1, N+1):
            sm += min(arr[i:j])

    assert sm == subarray_minimums_sum(arr)
