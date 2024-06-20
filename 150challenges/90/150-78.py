# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -10**8
        def DFS(node):
            nonlocal ans 
            if not node:
                return 0
            leftVal = DFS(node.left)
            rightVal = DFS(node.right)
            ans = max(ans,leftVal+node.val+rightVal,leftVal+node.val,rightVal+node.val,node.val)
            return max(leftVal+node.val,rightVal+node.val,node.val)
        DFS(root)
        return ans