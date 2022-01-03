from MyLinkedList import LinkedList


def partition(ll, n):
    before_start = None
    before_end = None
    after_start = None
    after_end = None
    node = ll.head
    while node is not None:
        next_node = node.next
        if node.data < n:
            if before_start is None:
                before_start = node
                before_end = before_start
                before_end.next = None
            else:
                before_end.next = node
                before_end = before_end.next
                before_end.next = None
        else:
            if after_start is None:
                after_start = node
                after_end = after_start
                after_end.next = None
            else:
                after_end.next = node
                after_end = after_end.next
                after_end.next = None
        node = next_node
    res_ll = LinkedList()
    if before_start is None:
        res_ll = after_start
    else:
        before_end.next = after_start
        res_ll.head = before_start
    return res_ll

def partition2(ll, n):
    node = ll.head
    head = ll.head
    tail = ll.head
    while node is not None:
        next_node = node.next
        if node.data < n:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
            tail.next = None
        node = next_node
    ll.head = head
    return ll

x = LinkedList.from_array([3, 5, 1, 8, 5, 10, 2, 1])
print(partition(x, 5))
x = LinkedList.from_array([3, 5, 1, 8, 5, 10, 2, 1])
print(partition2(x, 5))