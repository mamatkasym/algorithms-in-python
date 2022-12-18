"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k]
such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.
https://leetcode.com/problems/132-pattern/
"""


def find132pattern(self, nums: list[int]) -> bool:
    # we will find s1, s2, s3 such that s1 < s3 < s2
    # keep track of s3 such that it is maximum as possible
    s3 = float('-inf')

    # stack keeps non-increasing sequence of numbers
    stack = []
    for num in nums[::-1]:
        while stack and stack[-1] < num:
            s3 = max(s3, stack.pop())

        if num < s3 < stack[0]:
            return True

        stack.append(num)

    return False
