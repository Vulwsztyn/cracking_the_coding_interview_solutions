from Entities import *


def create_minimal_bst(arr):
    return create_minimal_bst_helper(arr, 0, len(arr) - 1)


def create_minimal_bst_helper(arr, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    node = TreeNode(arr[mid])
    node.left = create_minimal_bst_helper(arr, start, mid - 1)
    if node.left is not None:
        node.left.parent = node
    node.right = create_minimal_bst_helper(arr, mid + 1, end)
    if node.right is not None:
        node.right.parent = node
    return node


def in_order_successor(node):
    if node is None:
        return None
    if node.right is not None:
        n = node.right
        while n.left is not None:
            n = n.left
        return n.data
    else:
        p = node.parent
        n = node
        while p is not None and (p.left is None or p.left.data is not n.data):
            n = p
            p = p.parent
        return p.data


a = create_minimal_bst([x for x in range(11)])
a.right.right.right.right = TreeNode(100)
a.display()
print(in_order_successor(a), 5)
print(in_order_successor(a.left), 2)
print(in_order_successor(a.left.left), 0)
print(in_order_successor(a.left.left.right), 1)
print(in_order_successor(a.right.left.right), 7)
print(in_order_successor(a.right.right.right), 10)
