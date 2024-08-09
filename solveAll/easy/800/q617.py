# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        
        newRoot = TreeNode()
        r1left,r1right = None,None
        r2left,r2right = None,None
        if root1:
            newRoot.val += root1.val
            r1left = root1.left
            r1right = root1.right
        if root2:
            newRoot.val += root2.val
            r2left = root2.left
            r2right = root2.right
        
        newRoot.left = self.mergeTrees(r1left,r2left)
        newRoot.right = self.mergeTrees(r1right,r2right)
        return newRoot
