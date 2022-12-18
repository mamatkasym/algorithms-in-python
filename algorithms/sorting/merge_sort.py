"""
Worst case time complexity: O(n*log(n))
Average time complexity: O(n*log(n))
Tags: Divide and conquer, Two pointers

Algorithm:
    - Divide the unsorted array into subarray, each containing a single element.
    - Take adjacent pairs of two single-element array and merge them to form an array of 2 elements.
    - Repeat the process till a single sorted array is obtained.
"""


def merge(left: list[int], right: list[int]) -> list[int]:
    arr = []
    j = k = 0
    while j < len(left) and k < len(right):
        if left[j] < right[k]:
            arr.append(left[j])
            j += 1
        else:
            arr.append(right[k])
            k += 1

    arr += left[j:]
    arr += right[k:]
    return arr


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    b = merge_sort(arr[:mid])
    c = merge_sort(arr[mid:])
    return merge(b, c)


def faster_merge(arr: list[int], aux: list[int], lo: int, mid: int, hi: int):
    for i in range(lo, mid + 1):
        aux[i] = arr[i]

    for i in range(mid + 1, hi + 1):
        aux[i] = arr[hi - i + mid + 1]

    i, j = lo, hi
    for k in range(lo, hi + 1):
        if aux[j] < aux[i]:
            arr[k] = aux[j]
            j -= 1
        else:
            arr[k] = aux[i]
            i += 1


def faster_merge_sort(
    arr: list[int], aux: list[int], lo: int, hi: int
):  # Is not really fast, what is the source? TODO
    if lo == hi:
        return
    mid = (lo + hi) // 2
    faster_merge_sort(arr, aux, lo, mid)
    faster_merge_sort(arr, aux, mid + 1, hi)
    faster_merge(arr, aux, lo, mid, hi)


def iterative_merge_sort(arr: list[int]):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        iterative_merge_sort(left_arr)
        iterative_merge_sort(right_arr)

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1


def test():
    import random
    from time import time

    arr = [random.randint(1, 10**9) for _ in range(10**5)]
    iteratively = [x for x in arr]

    sorted_arr = list(sorted(arr))
    iterative_merge_sort(iteratively)
    t0 = time()
    recursively_sorted = merge_sort(arr)
    elapsed = time() - t0
    print("Elapsed time for merge sort", elapsed)

    aux = [0] * len(arr)
    t0 = time()
    faster_merge_sort(arr, aux, 0, len(arr) - 1)
    elapsed = time() - t0
    print("Elapsed time for faster merge sort", elapsed)

    assert arr == sorted_arr
    assert recursively_sorted == sorted_arr
    assert iteratively == sorted_arr
