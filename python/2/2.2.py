from MyLinkedList import LinkedList


def nth_to_last_recursive_logic(ll, n):
    if ll is None:
        return None, 0
    v, i = nth_to_last_recursive_logic(ll.next, n)
    i += 1
    if i == n:
        return ll.data, i
    return v, i


def nth_to_last_recursive(ll, n):
    return nth_to_last_recursive_logic(ll.head, n)[0]

def nth_to_last_iterative(ll, n):
    if ll is None:
        return None
    p1 = ll.head
    p2 = ll.head
    for i in range(n):
        if p2 is None:
            return None
        p2 = p2.next
    while p2 is not None:
        p1 = p1.next
        p2 = p2.next
    return p1.data


x = LinkedList.from_array([x for x in range(40)])
print(nth_to_last_recursive(x, 4))
print(nth_to_last_recursive(x, 3))
print(nth_to_last_recursive(x, 2))
print(nth_to_last_recursive(x, 1))
print(nth_to_last_iterative(x, 4))
print(nth_to_last_iterative(x, 3))
print(nth_to_last_iterative(x, 2))
print(nth_to_last_iterative(x, 1))