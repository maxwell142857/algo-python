# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkSame(node1,node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            else:
                return node1.val == node2.val and checkSame(node1.left,node2.left) and checkSame(node1.right,node2.right)
        
        d = deque()
        d.append(root)
        while d:
            node = d.popleft()
            result = checkSame(node,subRoot)
            if result:
                return True
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)
        return False