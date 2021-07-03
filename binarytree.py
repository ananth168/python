class TreeNode:
    def __init__(self, val, left, right) :
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def buildtree(self, inorder, preorder):
        if len(inorder) == 0:
            return None
        
        if len(preorder) == 1:
            last_node = TreeNode(preorder(0))
            return last_node

        ind = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[ind])

        node.left = self.buildtree(inorder[:ind], preorder)
        node.right = self.buildtree(inorder[ind+1:], preorder)


        return node