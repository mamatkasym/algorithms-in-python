import math


class RangeMinimumQuery:
    def __init__(self, arr: list[int]):
        """
        Build sparse table from given array.
        """

        # Sparse table: table[i][j] indicates minimum element in range [i, i + 2^j]
        row_size = len(arr)
        col_size = math.ceil(math.log2(len(arr))) + 1
        self.table = [[0] * col_size for _ in range(row_size)]

        for r in range(row_size):
            self.table[r][0] = arr[r]

        for c in range(1, col_size):
            _range = 2 ** c
            r = 0
            while r + _range < row_size:
                self.table[r][c] = min(self.table[r][c-1], self.table[r + 2**(c-1)][c-1])
                r += 1

    def get_minimum(self, _range: tuple[int, int]) -> int:
        left, right = _range
        block = int(math.log2(right + 1 - left))
        mid = right + 1 - (2 ** block)

        return min(self.table[left][block], self.table[mid][block])


def test():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    rmq = RangeMinimumQuery(arr)
    for _ in range(q):
        a, b = map(int, input().split())
        print(rmq.get_minimum((a-1, b-1)))

test()