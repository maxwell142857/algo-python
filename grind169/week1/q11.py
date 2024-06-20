
from collections import deque


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def getHeight(node):
            nonlocal balanced
            if not node:
                return 0
            left = getHeight(node.left)
            right = getHeight(node.right)
            if abs(left-right)>1:
                balanced = False
            return max(left,right)+1
        
        getHeight(root)
        return balanced