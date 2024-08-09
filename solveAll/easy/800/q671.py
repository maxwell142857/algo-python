# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root or not root.left:
            return -1
        
        left = self.findSecondMinimumValue(root.left)
        right = self.findSecondMinimumValue(root.right)

        if root.left.val == root.right.val:
            if left == -1 and right == -1:
                return -1
            elif left == -1:
                return right
            elif right == -1:
                return left
            else:
                return min(left,right)
        elif root.left.val == root.val:
            if left == -1:
                return root.right.val
            return min(left,root.right.val)
        else:
            if right == -1:
                return root.left.val
            return min(right,root.left.val)
        
