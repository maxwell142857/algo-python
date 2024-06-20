# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def longestPath(node):
            nonlocal ans
            if node == None:
                return 0
            
            left,right = 0,0
            if node.left:
                left = longestPath(node.left)+1
            if node.right:
                right = longestPath(node.right)+1
            ans = max(ans,left+right)
            return max(left,right)
        
        longestPath(root)
        return ans
        