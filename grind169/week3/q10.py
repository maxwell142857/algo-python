# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = float('-inf')
        flag = True

        def inOrderTravese(node):
            nonlocal flag,pre

            if not flag:
                return
            if not node:
                return
            
            inOrderTravese(node.left)

            if node.val <= pre:
                flag = False
            else:
                pre = node.val

            inOrderTravese(node.right)
        
        inOrderTravese(root)
        return flag