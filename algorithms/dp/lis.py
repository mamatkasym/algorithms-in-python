import bisect
from typing import Sequence


def longest_increasing_subsequence(seq: Sequence) -> list[int]:
    """
    :param seq: sequence ordered items
    :return: array of integers, length of the longest subsequence of each prefix
    TC: O(len(seq) ^ 2)
    MC: O(len(seq))
    """
    n = len(seq)
    # length[i] length of the longest increasing subsequence that ends at position i
    length = [1] * n
    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:
                length[i] = max(length[i], length[j] + 1)

    return length


def longest_increasing_subsequence_optimal(seq: Sequence) -> int:
    """
    :param seq: sequence of ordered items.
    :return: length of the longest subsequence.
    TC: O(len(seq) * log(len(seq)))
    MC: O(len(seq))
    """
    # d[i] is the smallest element at which an increasing subsequence of length i.
    d = [-float('inf')] + [float('inf')] * (len(seq))

    lis = 1
    for i, el in enumerate(seq):
        p = bisect.bisect_left(d, el)
        if d[p] >= el:
            d[p] = el
            lis = max(lis, p)

    return lis
