class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Binarytree():
    def __init__(self, value):
        self.root = Node(value)

    def Inorder(self, start, traversal):
        if start is None:
            return

        self.Inorder(start.left, traversal)
        traversal.append(start.value)
        self.Inorder(start.right, traversal)

        return traversal


tree = Binarytree(3)

tree.root.left = Node(7)
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)

tree.root.right = Node(8)
tree.root.right.left = Node(1)
tree.root.right.right = Node(5)

print(tree.Inorder(tree.root, []))

