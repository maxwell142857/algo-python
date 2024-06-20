# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ans = float('inf')
        def DFS(node):
            nonlocal cnt,ans
            if ans != float('inf'):
                # already find the answer
                return
            
            if node.left:
                DFS(node.left)
            cnt += 1
            if cnt == k:
                ans = node.val
            if node.right:
                DFS(node.right)

        DFS(root)
        return ans
        