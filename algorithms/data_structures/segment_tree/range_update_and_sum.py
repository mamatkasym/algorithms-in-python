
class RangeUpdateAndSum:
    def __init__(self, arr: list[int]):
        n = len(arr)
        self.n = n
        self.arr = arr
        self.tree = [0] * (4 * n)

        self._build(0, 0, n - 1)

    def _build(self, node: int, left: int, right: int):
        if left >= right:
            self.tree[node] = self.arr[left]
        else:
            mid = (left + right) // 2
            self._build(2 * node + 1, left, mid)
            self._build(2 * node + 2, mid + 1, right)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, left: int, right: int, start: int, stop: int, value: int):
        """
        Update elements between `start` and `stop` inclusive with `value`
        """
        pass

    def query(self, start: int, stop: int):
        """Return the sum of the elements between `start` and `stop` inclusive"""
        pass