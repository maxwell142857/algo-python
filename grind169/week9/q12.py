# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = float('-inf')
        def findSum(cur):
            nonlocal ans
            if not cur:
                return 0
            
            leftVal = findSum(cur.left)
            rightVal = findSum(cur.right)
            ans = max(ans,leftVal+cur.val,rightVal+cur.val,cur.val,leftVal+rightVal+cur.val)
            return max(leftVal+cur.val,rightVal+cur.val,cur.val)
        
        findSum(root)
        return ans