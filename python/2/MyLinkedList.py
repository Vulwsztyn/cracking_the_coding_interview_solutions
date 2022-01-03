class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def __str__(self):
        return self.__repr__()

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert(self, index, data):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = Node(data)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node

    @staticmethod
    def from_array(arr):
        list = LinkedList()
        current = Node(arr[0])
        list.head = current
        for i in arr[1:]:
            current.next = Node(i)
            current = current.next
        return list
