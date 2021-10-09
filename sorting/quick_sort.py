"""
Time complexity:
    Worst case: O(n)
    Average: O(n * lg(n))

It has advantage on sorting on placeQ, i.e. it does not require any extra storage
Applies divide and conquer paradigm
The key process is a partition
The worst case occurs when the partition process always picks greatest or smallest element as pivot
The best case occurs when the partition process always picks the middle element as pivot

Recurrences:
    Worst case: T(n) = T(n-1) + O(n)
    Best case: T(n) = 2T(n) + O(n) See how these recurrences are solved TODO
    Average: T(n) = T(9n/10) + T(n/10) + O(n)

Pseudo code:
    Divide: Divide the array A[p...r] into two -->  A[p...q-1] and A[q+1...r] such that
            each element of A[p...q-1] is less than or equal to A[q]
    Conquer: Sort the two subarrays A[p...q-1] and A[q+1...r] by recursive calls to quicksort
    Combine: Because the subarrays are already sorted, no work is needed to combine them:
             the entire array A[p....q] is now sorted.
"""
from typing import List
import random


def partition(A: List, p: int, r: int) -> int:
    # Select the last element in interval as a pivot element
    x = A[r]
    i = p - 1
    print('Partition:', A, p, '-->', r)
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            print('Partition step:', A)
    A[i+1], A[r] = A[r], A[i+1]
    print('Partition ends:', A)
    return i + 1


def partition_increasing(A: List, p: int, r: int) -> int:
    # Select the last element in interval as a pivot element
    x = A[r]
    i = p - 1
    print('Partition:', A, p, '-->', r)
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            print('Partition step:', A)
    A[i+1], A[r] = A[r], A[i+1]
    print('Partition ends:', A)
    return i + 1


def randomized_partition(A: List, p: int, r: int) -> int:
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)


def quicksort(A: List, p: int, r: int):
    if p < r:
        q = partition(A, p, r)
        print('Partitioned at', q)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def randomized_quicksort(A: List, p: int, r: int):
    if p < r:
        q = randomized_partition(A, p, r)
        print('Partitioned at', q)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


if __name__ == '__main__':
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quicksort(A, 0, len(A) - 1)
    print(A)
