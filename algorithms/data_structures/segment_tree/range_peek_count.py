class RangePeekCount:
    def __init__(self, arr: list[int]):
        self.arr = arr
        self.st = [0] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)

    def _get_value(self, idx):
        if (
            0 < idx < len(self.arr) - 1
            and self.arr[idx - 1] < self.arr[idx] < self.arr[idx + 1]
        ):
            return 1

        return 0

    def build(self, idx: int, lx, rx):
        if lx == rx:
            self.st[idx] = self._get_value(lx)

        left, right, mid = 2 * idx + 1, 2 * idx + 2, lx + (rx - lx) // 2
        self.build(left, lx, mid)
        self.build(right, mid + 1, rx)

        self.st[idx] = self.st[left] + self.st[right]

    def query(self, idx, lx, rx, lq, rq):
        if rx < lq or rq < lx:
            return 0
        if lx == lq and rx == rq:
            return self.st[idx]

        mid = lx + (rx - lx) // 2
        return self.query(2 * idx + 1, lx, mid, lq, rq) + self.query(
            2 * idx + 2, mid + 1, rx, lq, rq
        )
