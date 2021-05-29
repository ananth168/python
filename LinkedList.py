class Node:  # class to create node
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:  # class to create linked list
    def __init__(self):
        self.head = None


n1 = Node(3)
n2 = Node(5)
n3 = Node(4)
n4 = Node(8)

LL = LinkedList()

LL.head = n1
LL.head.next = n2
LL.head.next.next = n3
LL.head.next.next.next = n4

print(LL)
