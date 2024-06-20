class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkMirror(left,right):
            if not left and not right:
                return True
            elif left and right:
                return left.val== right.val and checkMirror(left.left,right.right) and checkMirror(left.right,right.left)
            else:
                return False
        return checkMirror(root.left,root.right)