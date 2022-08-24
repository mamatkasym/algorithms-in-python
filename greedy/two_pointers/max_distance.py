"""
Description: https://www.interviewbit.com/problems/max-distance/
"""


def max_distance(A: list[int]):
    n = len(A)
    # lm[a] is the leftmost index i, where A[i] = a
    lm = {}
    # rm[a] is the rightmost index i, where A[i] = a
    rm = {}
    # keep unique elements in A
    un = set()
    for i, a in enumerate(A):
        lm[a] = min(lm.get(a, n), i)
        rm[a] = max(lm.get(a, -1), i)
        un.add(a)
    ans = 0
    # current leftmost index we consider
    left = n
    # current rightmost index we consider
    right = -1
    for el in un:
        ans = max(ans, right - left)
        if lm[el] < left:
            right = rm[el]
            left = lm[el]
        elif rm[el] > right:
            right = rm[el]

    ans = max(ans, right - left)
    return ans
