# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ans = 0
        
        def tranverse(node):
            nonlocal cnt,k,ans
            if node.left:
                tranverse(node.left)
            cnt += 1
            if cnt == k:
                ans = node.val
            if node.right:
                tranverse(node.right)
        
        tranverse(root)
        return ans