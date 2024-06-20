# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def evaluate(cur):
            if cur.val == 0 :
                return False
            elif cur.val == 1:
                return True
            elif cur.val == 2:
                return evaluate(cur.left) or evaluate(cur.right)
            elif cur.val == 3:
                return evaluate(cur.left) and evaluate(cur.right)
            else:
                print('impossible')
        
        return evaluate(root)