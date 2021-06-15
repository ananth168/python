class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)


    

    def Preorder(self, start, traversal):    #root -> left -> right
        if start is None:
            return

        traversal.append(start.value)
        self.Preorder(start.left, traversal)  
        self.Preorder(start.right, traversal)  

        return traversal





tree = BinaryTree(3)

tree.root.left = Node(4)
tree.root.left.right = Node(2)
tree.root.left.left = Node(6)

tree.root.right = Node(7)
tree.root.right.right = Node(1)
tree.root.right.left = Node(9)

print(tree.Preorder(tree.root, []))
