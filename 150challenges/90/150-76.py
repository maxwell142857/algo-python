# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def DFS(node,target):
            if not node:
                return False
            target -= node.val
            if not node.left and not node.right:
                return target == 0
            else:
                return DFS(node.left,target) or DFS(node.right,target)
        return DFS(root,targetSum)