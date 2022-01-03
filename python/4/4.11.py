from Entities import *
import random


def create_minimal_bst(arr):
    return create_minimal_bst_helper(arr, 0, len(arr) - 1)


def create_minimal_bst_helper(arr, start, end):
    if end < start:
        return None, 0
    mid = (start + end) // 2
    node = TreeNode(arr[mid])
    node.left, left_size = create_minimal_bst_helper(arr, start, mid - 1)
    node.right, right_size = create_minimal_bst_helper(arr, mid + 1, end)
    node.size = left_size + right_size + 1
    return node, node.size


def get_node(node, index):
    left_size = node.left.size if node.left is not None else 0
    right_size = node.right.size if node.right is not None else 0
    if index < left_size:
        return get_node(node.left, index)
    elif index < left_size + right_size:
        return get_node(node.right, index - left_size)
    else:
        return node


def get_random_node(node):
    chosen = random.randrange(node.size)
    return get_node(node, chosen).data


a, _ = create_minimal_bst([x for x in range(10)])
a.display()
gotten = [0 for _ in range(10)]
for i in range(1000):
    gotten[get_random_node(a)] += 1
print(gotten)
