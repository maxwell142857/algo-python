# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def DFS(node,fromLeft):
            nonlocal ans
            if not node.left and not node.right and fromLeft:
                ans += node.val
            if node.left:
                DFS(node.left,True)
            if node.right:
                DFS(node.right,False)
        DFS(root,False)
        return ans
