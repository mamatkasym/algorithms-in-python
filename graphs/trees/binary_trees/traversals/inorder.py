from graphs.trees.binary_trees.ds import Node


def recursive(root: Node):
    if not root:
        return
    yield from recursive(root.left)
    yield root.val
    yield from recursive(root.right)


def iterative(root: Node):
    if not root:
        return
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            yield curr.val
            curr = curr.right


def test():
    tree = [5, 3, 7, 2, 4, 6, 8]
    tree = [Node(v) for v in tree]
    for i in range(3):
        tree[i].left = tree[2*i + 1]
        tree[i].right = tree[2*i + 2]

    order = [2, 3, 4, 5, 6, 7, 8]
    assert list(recursive(tree[0])) == order
    assert list(iterative(tree[0])) == order
