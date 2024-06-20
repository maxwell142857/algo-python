# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        first = True
        preVal = None
        ans = float('inf')
        def tranverse(node):
            nonlocal first, preVal, ans
            if node.left:
                tranverse(node.left)

            if first:
                first = False
                preVal = node.val
            else:
                ans = min(ans,abs(node.val-preVal))
                preVal = node.val
            if node.right:
                tranverse(node.right)
        
        tranverse(root)
        return ans
            