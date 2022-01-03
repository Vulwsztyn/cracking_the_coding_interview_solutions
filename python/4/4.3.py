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


def create_level_linked_list(root):
    lists = []
    create_level_linked_list_helper(root, lists, 0)
    return lists

def create_level_linked_list_helper(root, lists, level):
    if root is None:
        return
    while len(lists) <= level:
        lists.append([])
    lists[level].append(root.data)
    create_level_linked_list_helper(root.left, lists, level + 1)
    create_level_linked_list_helper(root.right, lists, level + 1)

def create_level_linked_list_recursive(root):
    result = []
    current = [root]
    while current: # current is not empty
        result.append([node.data for node in current])
        parents = current
        current = []
        for parent in parents:
            if parent.left is not None:
                current.append(parent.left)
            if parent.right is not None:
                current.append(parent.right)
    return result

a = create_minimal_bst([x for x in range(10)])
a.display()
print(create_level_linked_list(a))
print(create_level_linked_list_recursive(a))
