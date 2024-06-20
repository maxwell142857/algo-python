# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        ans = []
        while level:
            tmp = level[:]
            level.clear()
            ansLevel = []
            for node in tmp:
                ansLevel.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            ans.append(ansLevel)
        return ans
