# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        level = []
        if root:
            level.append(root)
        while level:
            ans.append(level[-1].val)
            tmp = level[:]
            level.clear()
            for node in tmp:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        return ans
            