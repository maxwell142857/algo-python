# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n)
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = float('inf')
        
        def DFS(cur):
            nonlocal ans
            if cur.left:
                DFS(cur.left)

            if abs(cur.val-target)<abs(ans-target):
                ans = cur.val
            
            if cur.right:
                DFS(cur.right)

        DFS(root)
        return ans
    
    # O(h), use BST's character
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        p = root
        ans = root.val
        while p:
            if abs(ans-target)>abs(p.val-target) or (abs(ans-target)==abs(p.val-target) and p.val<ans):
                ans = p.val
            if target==p.val:
                return target
            elif target<p.val:
                p = p.left
            else:
                p =p.right
        return ans
