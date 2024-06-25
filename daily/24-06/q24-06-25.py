# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # in-order traverse + preSum
    # O(n)
    def bstToGst(self, root: TreeNode) -> TreeNode:
        val = []

        def visit(node):
            if not node:
                return
            visit(node.left)
            val.append(node.val)
            visit(node.right)
        
        visit(root)

        n = len(val)
        sufSum = val[:]
        for i in range(n-2,-1,-1):
            sufSum[i] += sufSum[i+1]
        
        map = {}
        for i in range(n):
            map[val[i]] = sufSum[i]

        def update(node):
            if not node:
                return
            update(node.left)
            node.val = map[node.val]
            update(node.right)
        
        update(root)
        return root
        
    # reverse in order traverse
    # elegant 
    # O(n)
    def bstToGst(self, root: TreeNode) -> TreeNode:
        preSum = 0
        def visit(node):
            nonlocal preSum

            if not node:
                return
            
            visit(node.right)
            preSum += node.val
            node.val = preSum
            visit(node.left)
            
        visit(root)
        return root

