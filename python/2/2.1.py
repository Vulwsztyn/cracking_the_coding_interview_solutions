from MyLinkedList import LinkedList


def remove_duplicates(ll):
    element_set = set()
    previous = None
    current = ll.head
    while current:
        if current.data in element_set:
            previous.next = current.next
        else:
            element_set.add(current.data)
            previous = current
        current = current.next


def remove_duplicates2(ll):
    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


x = LinkedList.from_array([1, 2, 3, 1, 1, 3, 2, 3, 4, 5, 2])
remove_duplicates(x)
print(x)
x = LinkedList.from_array([1, 2, 3, 1, 1, 3, 2, 3, 4, 5, 2])
remove_duplicates2(x)
print(x)
