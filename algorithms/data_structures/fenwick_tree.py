"""
Properties:
    1. calculates the value of function F in the given range [L,R] (i.e. F(A[L], A[L+1],...,A[R])) in O(log(n)) time;
    2. updates the value of an element of A in O(log(n)) time;
    3. requires O(N) memory, or in other words, exactly the same memory required for A;
    4. is easy to use and code, especially, in the case of multidimensional arrays.
"""


class BinaryTreeNode:
    def __init__(self, lx: int, rx: int, val: int = 0):
        self.lx = lx
        self.rx = rx
        self.left: BinaryTreeNode | None = None
        self.right: BinaryTreeNode | None = None
        self.val = val


class FenwickTreeSum:
    def __init__(self, n):
        self.ft = [] * n

    def add(self, idx: int, val: int):
        pass

class FenwickTreePeeksCount:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.root = self.build_tree(0, len(nums) - 1)

    def build_tree(self, lx: int, rx: int):
        if lx > rx:
            return None

        if lx == rx:
            val = 1 if (0 < lx < len(self.nums) - 1 and self.nums[lx - 1] < self.nums[lx] < self.nums[lx + 1]) else 0
            return BinaryTreeNode(lx, rx, val)

        root: BinaryTreeNode = BinaryTreeNode(lx, rx)
        mid = (lx + rx) // 2
        left = self.build_tree(lx, mid)
        right = self.build_tree(mid + 1, rx)
        root.left, root.right, root.val = left, right, left.val + right.val

        return root

    def update_tree(self, root: BinaryTreeNode, index: int, value: int):
        if root.lx == root.rx == index:
            self.nums[index] = value
            val = 1 if (0 < index < len(self.nums) - 1 and self.nums[index - 1] < self.nums[index] < self.nums[index + 1]) else 0
            root.val = val
            return

        mid = root.lx + (root.rx - root.lx) // 2
        if mid > index:
            self.update_tree(root.right, index, value)
        else:
            self.update_tree(root.left, index, value)

        root.val = root.
