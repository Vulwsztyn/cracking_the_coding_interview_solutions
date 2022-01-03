def delete_node(node):
    if node is None or node.next is None:
        return None
    node.val = node.next.val
    node.next = node.next.next
    return node
