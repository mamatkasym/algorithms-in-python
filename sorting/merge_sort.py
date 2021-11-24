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


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    b = merge_sort(arr[:mid])
    c = merge_sort(arr[mid:])
    return merge(b, c)


def faster_merge(arr: List[int],  aux: List[int], lo: int, mid: int, hi: int):
    for i in range(lo, mid+1):
        aux[i] = arr[i]

    for i in range(mid+1, hi+1):
        aux[i] = arr[hi-i+mid+1]

    i, j = lo, hi
    for k in range(lo, hi+1):
        if aux[j] < aux[i]:
            arr[k] = aux[j]
            j -= 1
        else:
            arr[k] = aux[i]
            i += 1


def faster_merge_sort(arr: List[int], aux: List[int], lo: int, hi: int):  # Is not really fast TODO
    if lo == hi:
        return
    mid = (lo + hi) // 2
    faster_merge_sort(arr, aux, lo, mid)
    faster_merge_sort(arr, aux, mid+1, hi)
    faster_merge(arr, aux, lo, mid, hi)


def test():
    import random
    a = [random.randint(1, 10 ** 9) for _ in range(10 ** 5)]

    sorted_a = list(sorted(a))
    from time import time
    t0 = time()
    b = merge_sort(a)
    elapsed = time() - t0
    print('Elapsed time for merge sort', elapsed)

    aux = [0] * len(a)
    t0 = time()
    faster_merge_sort(a, aux, 0, len(a)-1)
    elapsed = time() - t0
    print('Elapsed time for faster merge sort', elapsed)

    assert a == sorted_a
    assert b == sorted_a
