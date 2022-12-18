class RangeSum:
    """Range sum segment tree implementation"""

    def __init__(self, arr: list[int]):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)

    def build(self, v: int, tl: int, tr: int):
        if tl >= tr:
            self.tree[v] = self.arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(2 * v + 1, tl, tm)
            self.build(2 * v + 2, tm + 1, tr)
            self.tree[v] = self.tree[2 * v + 1] + self.tree[2 * v + 2]

    def update(self, v: int, tl: int, tr: int, pos: int, new_val: int):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v*2, tl, tm, pos, new_val)
            else:
                self.update(v*2+1, tm+1, tr, pos, new_val)

            self.tree[v] = self.tree[v*2] + self.tree[v*2+1]

    def sum(self, v: int, tl: int, tr: int, le: int, r: int):
        """
        Return arr[l] + arr[l+1] + ... + arr[r]
        """
        if le > r:
            return 0
        if le == tl and r == tr:
            return self.tree[v]

        tm = (tl + tr) // 2
        return self.sum(v * 2 + 1, tl, tm, le, min(r, tm)) + self.sum(
            v * 2 + 2, tm + 1, tr, max(le, tm + 1), r
        )


def test_st():
    a = [2, 4, 7, 1, 1, 6, 3, 2, 8, 3, 1]
    st = RangeSum(a)
    assert st.sum(0, 0, len(a), 2, 5) == 15
    assert st.sum(0, 0, len(a), 3, 4) == 2
    assert st.sum(0, 0, len(a), 0, len(a)) == sum(a)
    assert st.sum(0, 0, len(a), 1, 1) == 4
