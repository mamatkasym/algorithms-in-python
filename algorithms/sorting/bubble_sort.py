from typing import List


def bubble_sort(arr: List[int]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


def test():
    a = [2, 4, 1, 7, 3, 4, 2, 6, 3]
    bubble_sort(a)
    b = sorted(a)
    assert a == b
