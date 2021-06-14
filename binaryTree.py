class Node():
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)


tree =  BinaryTree(3)

tree.root.left = Node(4)
tree.root.left.right = Node(8)
tree.root.left.left = Node(9)

tree.root.right = Node(5)
tree.root.right.right = Node(21)
tree.root.right.left = Node(19)

print('\ntree is at: ', tree)
        