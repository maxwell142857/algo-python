# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(node,result):
            if not node.left and not node.right:
                result.append(node.val)
                return
            
            if node.left:
                getLeaves(node.left,result)
            if node.right:
                getLeaves(node.right,result)
        
        leaves1,leaves2 = [],[]
        getLeaves(root1,leaves1)
        getLeaves(root2,leaves2)
        if len(leaves1) != len(leaves2):
            return False
        for i in range(len(leaves1)):
            if leaves1[i] != leaves2[i]:
                return False
        return True