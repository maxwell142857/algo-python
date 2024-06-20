# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        
        def DFS(node):
            nonlocal ans
            if not node:
                return False
            
            left = DFS(node.left)
            right = DFS(node.right)
            if node == p or node == q:
                if left or right:
                    ans = node
                
                return True
            else:
                if left and right:
                    ans = node
                    return True
                elif left or right:
                    return True
                else:
                    return False
        
        DFS(root)
        return ans