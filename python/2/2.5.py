from MyLinkedList import LinkedList, Node


def add_lists_backwards_logic(l1, l2, c):
    if l1 is None and l2 is None and c == 0:
        return None
    v1 = l1.data if l1 is not None else 0
    v2 = l2.data if l2 is not None else 0
    n1 = l1.next if l1 is not None else None
    n2 = l2.next if l2 is not None else None
    s = v1 + v2 + c
    node = Node(s % 10)
    node.next = add_lists_backwards_logic(n1, n2, s // 10)
    return node


def add_lists_backwards(l1, l2):
    node = add_lists_backwards_logic(l1.head, l2.head, 0)
    ll = LinkedList()
    ll.head = node
    return ll


def length(node):
    return 0 if node is None else length(node.next) + 1


def insert_before(node, v):
    n = Node(v)
    if node is not None:
        n.next = node
    return n


def zero_pad(node, padding):
    head = node
    for _ in range(padding):
        head = insert_before(head, 0)
    return head


def add_lists_helper(l1, l2):
    if l1 is None and l2 is None:
        return None, 0
    s, carry = add_lists_helper(l1.next, l2.next)
    v = carry + l1.data + l2.data
    res = insert_before(s, v % 10)
    return res, v // 10


def add_lists_forward(l1, l2):
    len1 = length(l1.head)
    len2 = length(l2.head)
    l1 = zero_pad(l1.head, len2 - len1)
    l2 = zero_pad(l2.head, len1 - len2)

    s, c = add_lists_helper(l1, l2)
    if c:
        s = insert_before(s, c)
    res_l = LinkedList()
    res_l.head = s
    return res_l


print(add_lists_backwards(LinkedList.from_array([7, 1, 6]), LinkedList.from_array([5, 9, 2])))
print(add_lists_forward(LinkedList.from_array([1, 2, 3, 4]), LinkedList.from_array([5, 6, 7])))
