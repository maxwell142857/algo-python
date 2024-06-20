# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        level = []
        level.append(root)
        ans = root.val
        while level:
            tmp = level[:]
            level.clear()
            for node in tmp:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                ans = level[0].val
        return ans