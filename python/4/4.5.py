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


def check_bst(root):
    return check_bst_helper(root, None, None)


def check_bst_helper(root, min_threshold, max_threshold):
    if root is None:
        return True
    if min_threshold is not None and root.data <= min_threshold:
        return False
    if max_threshold is not None and root.data >= max_threshold:
        return False
    return check_bst_helper(root.left, min_threshold, root.data) and check_bst_helper(root.right, root.data, max_threshold)


a = create_minimal_bst([x for x in range(10)])
a.right.right.right.right = TreeNode(100)
a.display()
print(check_bst(a))
a.left.right.right.right = TreeNode(4)
a.display()
print(check_bst(a))
