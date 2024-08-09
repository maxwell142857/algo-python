# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def find(node,val):
            if not node:
                return False
            
            if node.val == val:
                return True
            elif val>node.val:
                return find(node.right,val)
            else:
                return find(node.left,val)
        
        ans = False

        def traverse(node):
            nonlocal ans
            if not node or ans:
                return
            
            if node.val*2 != k and find(root,k-node.val):
                ans = True
                return
            
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return ans