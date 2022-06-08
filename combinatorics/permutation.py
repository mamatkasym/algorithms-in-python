"""
Find all permutation of array [1, 2, 3, ..., n]
"""
from typing import List, MutableSequence
from copy import copy
from itertools import permutations


def permute(pos: int, arr: MutableSequence, n: int, result: List):
    if pos == n:
        result.append(tuple(copy(arr)))
    else:
        for j in range(pos, n):
            arr[pos], arr[j] = arr[j], arr[pos]
            permute(pos + 1, arr, n, result)
            arr[pos], arr[j] = arr[j], arr[pos]


class AllPermutations:
    result: List = []

    def permute(self, pos, arr, n):
        if pos == n:
            self.result.append(arr.copy())
        else:
            for j in range(pos, n):
                arr[pos], arr[j] = arr[j], arr[pos]
                self.permute(pos + 1, arr, n)
                arr[pos], arr[j] = arr[j], arr[pos]

    def get_all(self, n):
        if not n:
            return []
        arr = [i + 1 for i in range(n)]
        self.permute(0, arr, n)
        return self.result


def test():
    iterable = [1, 2, 3, 4]
    _permutations = []
    permute(0, iterable, 4, _permutations)
    assert len(_permutations) == 24
    assert sorted(list(permutations(iterable))) == sorted(
        _permutations
    )  # TODO check without sorted
