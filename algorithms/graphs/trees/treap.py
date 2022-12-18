class Treap:
    x: int
    y: int
    left: None
    right: None

    def __init__(self, x, y):
        self.x = x
        self.y = y


def split(t: Treap, k: int) -> (Treap, Treap):
    """
    A function that returns tuple of treaps (T1, T2), such that all keys in T1 are less than k and T2 contains
    all other
    Time complexity is O(h) where h is the height of the treap
    """
    if not t:
        return None, None
    elif k > t.x:
        t1, t2 = split(t.right, k)
        t.right = t1
        return t, t2
    else:
        t1, t2 = split(t.left, k)
        t.left = t2
        return t1, t


def merge(t1: Treap, t2: Treap) -> Treap:
    """
    Merges two treaps and returns it
    Time complexity O(h) where h is the height of the treap
    """
    if not t2:
        return t1
    if not t1:
        return t2
    elif t1.y > t2.y:
        t1.right = merge(t1.right, t2)
        return t1
    else:
        t2.left = merge(t1, t2.left)
        return t2


def insert(t: Treap, x: int, y: int) -> Treap:
    t1, t2 = split(t, x)
    t1 = merge(t1, Treap(x, y))
    return merge(t1, t2)


# def remove(t: Treap, x: int) -> Treap:
#     pass
