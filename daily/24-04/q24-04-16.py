# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        level = [root]
        levelCnt = 1
        while levelCnt != depth-1:
            tmp  = level[:]
            level.clear()
            for node in tmp:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            levelCnt += 1
        for node in level:
            leftTree = node.left
            rightTree = node.right
            node.left = TreeNode(val,leftTree,None)
            node.right = TreeNode(val,None,rightTree)
        return root