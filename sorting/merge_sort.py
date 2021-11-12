from typing import List


def merge(L, R):
    arr = []
    j = k = 0
    while j < len(L) and k < len(R):
        if L[j] < R[k]:
            arr.append(L[j])
            j += 1
        else:
            arr.append(R[k])
            k += 1

    arr += L[j:]
    arr += R[k:]
    return arr


def merge_sort(arr: List):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    b = merge_sort(arr[:mid])
    c = merge_sort(arr[mid:])
    return merge(b, c)


def test():
    a = [2, 4, 1, 3, 7, 8, 4, 5, 2]
    assert merge_sort(a) == list(sorted(a))


test()
