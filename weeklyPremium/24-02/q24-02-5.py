# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        ans = 0

        # check wether this node is the answer, return the sum of subtree
        def DFS(node):
            nonlocal ans
            if not node:
                return 0
            
            leftSum = DFS(node.left)
            rightSum = DFS(node.right)
            if leftSum+rightSum==node.val:
                ans += 1
            return leftSum+rightSum+node.val
        
        DFS(root)
        return ans
