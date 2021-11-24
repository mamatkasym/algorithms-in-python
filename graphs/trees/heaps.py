"""
A binary heap is a special data structure that resembles a binary tree.
It differs in the sense that the root of any subtree should be the smallest or the largest element.
"""


class Heap:
    key: int
    left: None
    right: None


class MaxHeap:
    """
    List implementation of Max heap data structure
    """
    def __init__(self):
        self.heap = []

    @staticmethod
    def parent_position(i):
        return int((i - 1) / 2)

    @staticmethod
    def left_child_position(i):
        return 2 * i + 1

    @staticmethod
    def right_child_position(i):
        return 2 * i + 2

    def has_parent(self, i):
        return self.parent_position(i) < len(self.heap)

    def has_left_child(self, i):
        return self.left_child_position(i) < len(self.heap)

    def has_right_child(self, i):
        return self.right_child_position(i) < len(self.heap)

    def print(self):
        print(self.heap)

    def push(self, item):
        self.heap.append(item)
        self._siftdown(0, len(self.heap) - 1)

    def _siftdown(self, start_pos, pos):
        # Max heap variant of _siftdown
        new_item = self.heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # new item fits.
        while pos > start_pos:
            parent_pos = (pos - 1) >> 1
            parent = self.heap[parent_pos]
            if parent < new_item:
                self.heap[pos] = parent
                pos = parent_pos
                continue
            break
        self.heap[pos] = new_item

    def pop(self):
        """Pop the largest item off the heap, maintaining the heap invariant."""
        last = self.heap.pop()  # raises appropriate IndexError if heap is empty
        if self.heap:
            return_item = self.heap[0]
            self.heap[0] = last
            self._siftup(0)
            return return_item
        return last

    def _siftup(self, pos):
        """Max heap variant of _siftup"""
        end_pos = len(self.heap)
        start_pos = pos
        new_item = self.heap[pos]
        # Bubble up the larger child until hitting a leaf.
        child_pos = 2 * pos + 1  # leftmost child position
        while child_pos < end_pos:
            # Set child_pos to index of larger child.
            right_pos = child_pos + 1
            if right_pos < end_pos and not self.heap[right_pos] < self.heap[child_pos]:
                child_pos = right_pos
            # Move the larger child up.
            self.heap[pos] = self.heap[child_pos]
            pos = child_pos
            child_pos = 2 * pos + 1
        # The leaf at pos is empty now.  Put new item there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.heap[pos] = new_item
        self._siftdown(start_pos, pos)
