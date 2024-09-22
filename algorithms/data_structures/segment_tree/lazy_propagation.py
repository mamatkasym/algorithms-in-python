
class LazyPropagation:
    """
    Lazy propagation for range sum segment tree.
    """
    def __init__(self, arr: list):
        """
        Note that index of root of the segment tree is 1.
        """
        self.arr = arr
        self.lazy = [0] * (4 * len(arr))
        self.tree = [0] * (4 * len(arr))

        self.build(1, 1, len(arr))

    def build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = self.arr[start]
            return

        mid = (start + end) // 2
        left, right = 2 * node, 2 * node + 1
        self.build(left, start, mid)
        self.build(right, mid + 1, end)

        self.tree[node] = self.tree[left] + self.tree[right]

    def update(self, node: int, start: int, end: int, left: int, right: int, val: int):
        """
        Update values from index `start` to `end` with `val`.
        """
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
