"""

"""
import copy
from graphs.trees.binary_trees.ds import Node
from graphs.trees.binary_trees.traversals import inorder


def bst_minimum(root: Node) -> Node or None:
    """Return node with minimum value in given bst"""
    if not root:
        return root
    while root.left:
        root = root.left
    return root


def bst_maximum(root: Node) -> Node or None:
    """Return node with maximum value in given bst"""
    if not root:
        return root
    while root.right:
        root = root.right
    return root


def delete_node_iterative(root: Node, key: int) -> Node:
    """
    delete node with value key from bst with root root
    The time complexity of the above solution is O(n), where n is the size of the BST.
    The auxiliary space required by the program is O(n) for recursion (call stack).
    """
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
        successor = bst_minimum(curr.right)
        val = successor.val
        delete_node_iterative(curr, val)
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


def delete_node_recursive(root: Node, key: int) -> Node or None:
    """
    delete node with value key from bst with root root
    The time complexity of the above solution is O(n), where n is the size of the BST,
    and requires space proportional to the tree’s height for the call stack
    """
    if not root:
        return root
    if key < root.val:
        root.left = delete_node_recursive(root.left, key)
    elif key > root.val:
        root.right = delete_node_recursive(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left and root.right:
            predecessor = bst_maximum(root.left)
            root.val = predecessor.val
            root.left = delete_node_recursive(root.left, predecessor.val)
        else:
            child = root.left if root.left else root.right
            root = child
    return root


def insert_node_recursive(root: Node, key: int) -> Node:
    """
    The time complexity is O(h), where h is the BST height.
    The space complexity is also O(h).
    """
    if not root:
        return Node(key)
    if key < root.val:
        root.left = insert_node_recursive(root.left, key)
    else:
        root.right = insert_node_recursive(root.right, key)

    return root


def insert_node_iterative(root: Node, key: int) -> Node:
    """
    The time complexity is O(h), where h is the BST height.
    The space complexity is also O(1).
    """
    curr = root

    # pointer to store the parent of the current node
    parent = None

    # if the tree is empty, create a new node and set it as root
    if root is None:
        return Node(key)

    # traverse the tree and find the parent node of the given key
    while curr:

        # update the parent to the current node
        parent = curr

        # if the given key is less than the current node,
        # go to the left subtree; otherwise, go to the right subtree.
        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    # construct a node and assign it to the appropriate parent pointer
    if key < parent.data:
        parent.left = Node(key)
    else:
        parent.right = Node(key)

    return root


def test_delete_node():
    values = [5, 3, 8, 1, 4, 6, 9, None, 2, None, None, None, 7]
    nodes = [Node(v) if v else None for v in values]
    for i in range(len(nodes)):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    # delete root
    tree = copy.deepcopy(nodes)
    res = delete_node_iterative(tree[0], 5)
    assert list(inorder.recursive(res)) == [1, 2, 3, 4, 6, 7, 8, 9]
    # delete node with two children
    tree = copy.deepcopy(nodes)
    res = delete_node_iterative(tree[0], 3)
    assert list(inorder.recursive(res)) == [1, 2, 4, 5, 6, 7, 8, 9]
    # delete node with one children
    tree = copy.deepcopy(nodes)
    res = delete_node_iterative(tree[0], 6)
    assert list(inorder.recursive(res)) == [1, 2, 3, 4, 5, 7, 8, 9]
    # delete leaf node
    tree = copy.deepcopy(nodes)
    res = delete_node_iterative(tree[0], 2)
    assert list(inorder.recursive(res)) == [1, 3, 4, 5, 6, 7, 8, 9]

    # delete root
    tree = copy.deepcopy(nodes)
    res = delete_node_recursive(tree[0], 5)
    assert list(inorder.recursive(res)) == [1, 2, 3, 4, 6, 7, 8, 9]
    # delete node with two children
    tree = copy.deepcopy(nodes)
    res = delete_node_recursive(tree[0], 3)
    assert list(inorder.recursive(res)) == [1, 2, 4, 5, 6, 7, 8, 9]
    # delete node with one children
    tree = copy.deepcopy(nodes)
    res = delete_node_recursive(tree[0], 6)
    assert list(inorder.recursive(res)) == [1, 2, 3, 4, 5, 7, 8, 9]
    # delete leaf node
    tree = copy.deepcopy(nodes)
    res = delete_node_recursive(tree[0], 2)
    assert list(inorder.recursive(res)) == [1, 3, 4, 5, 6, 7, 8, 9]
