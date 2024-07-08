# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        
        def build(cur):
            if not cur:
                return [None,None]
            
            if cur.val>target:
                # splite the left sub tree
                res = build(cur.left)
                cur.left = res[1]
                return [res[0],cur]
            else:
                # splite the right sub tree
                res = build(cur.right)
                cur.right = res[0]
                return[cur,res[1]]
        return build(root)
            



