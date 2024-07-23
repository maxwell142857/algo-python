# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # create new tree
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummyHead = TreeNode()
        p = dummyHead

        def traverse(node):
            nonlocal p
            if not node:
                return 
            
            traverse(node.left)

            p.right = TreeNode(node.val)
            p = p.right

            traverse(node.right)
        
        traverse(root)
        return dummyHead.right

    # on the fly
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def traverse(node,parent):
            if not node:
                return 
            
            traverse(node.left)

            p.right = TreeNode(node.val)
            p = p.right

            traverse(node.right)
        