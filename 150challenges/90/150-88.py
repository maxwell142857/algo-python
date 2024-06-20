# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# from bottom to top
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans  =True

        def check(node):
            nonlocal ans
            if ans:
                rangeLeft = [] #  [min,max]
                rangeRight = [] #  [min,max]
                if node.left:
                    rangeLeft = check(node.left)
                if node.right:
                    rangeRight  =check(node.right)
            
                if len(rangeLeft)==0 and len(rangeRight)==0:
                    return [node.val,node.val]
                elif len(rangeLeft) == 0:
                    if node.val>= rangeRight[0]:
                        ans = False
                    return [node.val,rangeRight[1]]
                elif len(rangeRight) == 0:
                    if node.val<= rangeLeft[1]:
                        ans = False
                    return [rangeLeft[0],node.val]
                else:
                    if node.val>=rangeRight[0] or node.val<=rangeLeft[1]:
                        ans = False
                    return [rangeLeft[0],rangeRight[1]]
            else:
                return []
        
        check(root)
        return ans
    
# from top to bottom
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node,low = float('-inf'),high = float('inf')):
            if not node:
                return True 
            if node.val > low and node.val < high:
                return check(node.left,low,node.val) and check(node.right,node.val,high)
            else:
                return False
            
        return check(root)