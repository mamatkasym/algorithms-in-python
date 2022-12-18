from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, val: T):
        self.val = val
        self.left = None
        self.right = None
