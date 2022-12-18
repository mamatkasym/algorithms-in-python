import math


class GcdST:
    """Max segment tree implementation"""

    def __init__(self, arr: list[int]):
        self.arr = arr
        self.tree = [1] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)

    def build(self, v: int, tl: int, tr: int):
        if tl >= tr:
            self.tree[v] = self.arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(2 * v + 1, tl, tm)
            self.build(2 * v + 2, tm + 1, tr)
            self.tree[v] = math.gcd(self.tree[2 * v + 1], self.tree[2 * v + 2])

    def get_gcd(self, v: int, tl: int, tr: int, le: int, r: int) -> int:
        """Returns GCD(a[l], ..., a[r])"""
        if tl > r or tr < le:
            return 0
        if le <= tl and r >= tr:
            return self.tree[v]

        tm = (tl + tr) // 2
        return math.gcd(
            self.get_gcd(v * 2 + 1, tl, tm, le, min(r, tm)),
            self.get_gcd(v * 2 + 2, tm + 1, tr, max(le, tm + 1), r),
        )


def test_st():
    from random import randint

    n = 100
    a = [randint(1, 1000) for _ in range(n)]
    st = GcdST(a)
    for i in range(n):
        for j in range(i, n):
            assert st.get_gcd(0, 0, n - 1, i, j) == math.gcd(*a[i: j + 1])
