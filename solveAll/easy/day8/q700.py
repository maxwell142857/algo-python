# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = None
        def traverse(node):
            nonlocal ans
            if (not node) or ans:
                return 
            
            if node.val == val:
                ans = node
                return
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return ans
            
    # o(h)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        p = root
        while p:
            if p.val > val:
                p = p.left
            elif p.val == val:
                return p
            else:
                p = p.right
        return None
