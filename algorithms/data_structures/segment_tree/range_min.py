class RangeMinimumQuery:
    """
    Range minimum query segment tree implementation
    """
    # This value may depend on problem constraints
    MAX_INT: int = 10 ** 10

    def __init__(self, arr: list[int]):
        self.arr = arr
        self.tree = [(0, 0)] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)

    @staticmethod
    def combine(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
        if a[0] < b[0]:
            return a
        elif b[0] < a[0]:
            return b

        return a[0], a[1] + b[1]

    def build(self, v: int, tl: int, tr: int):
        if tl >= tr:
            self.tree[v] = (self.arr[tl], 1)
        else:
            tm = (tl + tr) // 2
            self.build(2 * v + 1, tl, tm)
            self.build(2 * v + 2, tm + 1, tr)
            self.tree[v] = self.combine(self.tree[2 * v + 1], self.tree[2 * v + 2])

    def update(self, v: int, tl: int, tr: int, pos: int, new_val: int):
        """
        Update the value of the array at position `pos` with `new_value` and
        the segment tree as well.
        """
        if tl == tr:
            self.tree[v] = (new_val, 1)
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v * 2 + 1, tl, tm, pos, new_val)
            else:
                self.update(v * 2 + 2, tm + 1, tr, pos, new_val)

            self.tree[v] = self.combine(self.tree[v * 2 + 1], self.tree[v * 2 + 2])

    def get_min(self, v: int, tl: int, tr: int, le: int, r: int) -> tuple[int, int]:
        """
        Returns minimum value in range l...r and its frequency
        """

        if le > r:
            return self.MAX_INT, 0
        if le == tl and r == tr:
            return self.tree[v]

        tm = (tl + tr) // 2
        return self.combine(
            self.get_min(v * 2 + 1, tl, tm, le, min(r, tm)),
            self.get_min(v * 2 + 2, tm + 1, tr, max(le, tm + 1), r),
        )


def test_st():
    a = [2, 4, 7, 1, 1, 6, 8, 2, 8, 3, 1]
    st = RangeMinimumQuery(a)
    assert st.get_min(0, 0, len(a), 2, 5) == (7, 1)
    assert st.get_min(0, 0, len(a), 3, 4) == (1, 2)
    assert st.get_min(0, 0, len(a), 0, len(a)) == (8, 2)
    assert st.get_min(0, 0, len(a), 0, 1) == (4, 1)

# TODO: implement lazy propagation version
