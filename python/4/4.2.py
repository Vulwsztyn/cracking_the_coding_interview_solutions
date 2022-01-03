from Entities import *

def create_minimal_bst(arr):
    return create_minimal_bst_helper(arr, 0, len(arr) - 1)

def create_minimal_bst_helper(arr, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    node = TreeNode(arr[mid])
    node.left = create_minimal_bst_helper(arr, start, mid - 1)
    node.right = create_minimal_bst_helper(arr, mid + 1, end)
    return node

a = create_minimal_bst([x for x in range(10)])
b = create_minimal_bst([x for x in range(11)])
c = create_minimal_bst([x for x in range(12)])
a.display()
b.display()
c.display()

