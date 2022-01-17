"""

"""
import copy
from graphs.trees.binary_trees.ds import Node
from graphs.trees.binary_trees.traversals import inorder


def tree_minimum(root: Node) -> Node:
    """ Return node with minimum value in given tree """
    if not root:
        return root
    while root.left:
        root = root.left
    return root


def delete_node(root: Node, key: int) -> Node:
    parent = None
    curr = root

    while curr and curr.val != key:
        parent = curr
        if curr.val < key:
            curr = curr.right
        else:
            curr = curr.left

    if curr is None:
        return root
    # Case 1: If both children are null
    if curr.left is None and curr.right is None:
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        else:
            root = None

    # Case 2: If both children are not null
    elif curr.left and curr.right:
        successor = tree_minimum(curr.right)
        val = successor.val
        delete_node(curr, val)
        curr.val = val
    # Case 3: If only one of the children if not null
    else:
        if curr.left:
            child = curr.left
        else:
            child = curr.right

        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            root = child
    return root


def test_delete_node():
    values = [5, 3, 8, 1, 4, 6, 9, None, 2, None, None, None, 7]
    nodes = [Node(v) if v else None for v in values]
    for i in range(len(nodes)):
        if 2*i + 1 < len(nodes):
            nodes[i].left = nodes[2*i+1]
        if 2*i + 2 < len(nodes):
            nodes[i].right = nodes[2*i+2]
    # delete root
    tree = copy.deepcopy(nodes)
    res = delete_node(tree[0], 5)
    assert list(inorder.recursive(res)) == [1, 2, 3, 4, 6, 7, 8, 9]
    # delete node with two children
    tree = copy.deepcopy(nodes)
    res = delete_node(tree[0], 3)
    assert list(inorder.recursive(res)) == [1, 2, 4, 5, 6, 7, 8, 9]
    # delete node with one children
    tree = copy.deepcopy(nodes)
    res = delete_node(tree[0], 6)
    assert list(inorder.recursive(res)) == [1, 2, 3, 4, 5, 7, 8, 9]
    # delete leaf node
    tree = copy.deepcopy(nodes)
    res = delete_node(tree[0], 2)
    assert list(inorder.recursive(res)) == [1, 3, 4, 5, 6, 7, 8, 9]
