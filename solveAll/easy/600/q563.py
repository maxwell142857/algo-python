# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0
        def getSum(node):
            nonlocal tilt
            if not node:
                return 0
            
            leftSum = getSum(node.left)
            rightSum = getSum(node.right)
            tilt += abs(leftSum-rightSum)

            return leftSum+rightSum+node.val
        
        getSum(root)
        return tilt
            