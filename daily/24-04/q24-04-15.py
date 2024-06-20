# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def DFS(node,sum):
            nonlocal ans
            sum = sum*10+node.val
            if not node.left and not node.right:
                ans += sum
                return
            if node.left:
                DFS(node.left,sum)
            if node.right:
                DFS(node.right,sum)

        DFS(root,0)
        return ans