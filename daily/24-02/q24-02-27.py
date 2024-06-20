from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1

        def DFS(node):
            nonlocal ans
            if not node:
                return 0
            leftL = DFS(node.left)
            rightL = DFS(node.right)
            ans = max(ans,leftL+rightL+1)
            return 1+max(leftL,rightL)
        
        DFS(root)
        return ans
