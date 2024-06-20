# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def find(node,current):
            nonlocal ans
            if node == None:
                ans = max(ans,current)
            else:
                find(node.left,current+1)
                find(node.right,current+1)
        
        find(root,0)
        return ans