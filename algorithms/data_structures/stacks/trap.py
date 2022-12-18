from typing import List


def trap(h: List[int]) -> int:
    R = [x for x in h]
    L = [x for x in h]
    for i in range(1, len(h)):
        L[i] = max(L[i-1], h[i])

    for i in range(len(h)-2, -1, -1):
        R[i] = max(R[i+1], h[i])

    ans = 0
    for i in range(len(h)):
        ans += min(R[i], L[i]) - h[i]

    return ans


print(trap([]))
