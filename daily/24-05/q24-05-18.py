# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        # input: a node as root
        # output: a val, positive means it can give you;negative means it need from you
        def DFS(cur):
            nonlocal cnt
            if not cur:
                return 0
            
            leftVal = DFS(cur.left)
            rightVal = DFS(cur.right)
            cnt += abs(leftVal+rightVal+cur.val-1)
            return leftVal+rightVal+cur.val-1
        
        DFS(root)
        return cnt


        
