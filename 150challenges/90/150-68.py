# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def findDepth(node):
            if not node:
                return 0
            return max(findDepth(node.left)+1,findDepth(node.right)+1)

        return findDepth(root)