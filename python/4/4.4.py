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


def is_balanced(root):
    return is_balanced_helper(root)[0]


def is_balanced_helper(root):
    if root is None:
        return True, 0
    left_is_balance, left_height = is_balanced_helper(root.left)
    if not left_is_balance:
        return False, 0
    right_is_balance, right_height = is_balanced_helper(root.right)
    if not right_is_balance:
        return False, 0
    return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1


a = create_minimal_bst([x for x in range(10)])
a.display()
print(is_balanced(a))
a.right.right.right.right = TreeNode(100)
a.display()
print(is_balanced(a))
