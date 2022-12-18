from typing import Sequence


def longest_increasing_subsequence(seq: Sequence) -> list[int]:
    """
    :param seq: sequence ordered items
    :return: array of integers, length of longest subsequence of each prefix
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


def longest_increasing_subsequence_optimal(seq: Sequence) -> list[int]:  # TODO
    """
    :param seq: sequence ordered items
    :return: array of integers, length of longest subsequence of each prefix
    TC: O(len(seq) * log(len(seq)))
    MC: O(len(seq))
    """
