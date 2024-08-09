# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        pre = -10**5-1
        diff = 10**5+1

        def inOrderTraverse(node):
            nonlocal pre, diff
            if node.left:
                inOrderTraverse(node.left)
            
            diff = min(diff,abs(node.val-pre))
            pre = node.val

            if node.right:
                inOrderTraverse(node.right)

        inOrderTraverse(root)
        return diff