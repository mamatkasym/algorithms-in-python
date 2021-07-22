from typing import List


def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
def merge_sort(a: List):
    if len(a) == 1:
        return a
    n = len(a)
    b = merge_sort(a[:n//2])
    c = merge_sort(a[n//2:])
    if b[0] >= c[-1]:
        return c + b
    else:
        return b + c

a = list(map(int, input().split()))
print(merge_sort(a))