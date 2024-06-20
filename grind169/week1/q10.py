# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # do not consider it as BST
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def DFS(node):
            nonlocal ans
            if ans:
                return False
            if not node:
                return False
            
            leftResult = DFS(node.left)
            rightResult = DFS(node.right)
            myself = node == p or node == q
            if myself and (leftResult or rightResult):
                ans = node
            if leftResult and rightResult:
                ans = node
            return leftResult or rightResult or myself
        
        DFS(root)
        return ans

    # use BST's feature
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':     
        pointer = root
        while True:
            if pointer.val>p.val and pointer.val>q.val:
                pointer = pointer.left
            elif pointer.val<p.val and pointer.val<q.val:
                pointer = pointer.right
            else:
                return pointer