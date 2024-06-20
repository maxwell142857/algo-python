# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = [root]
        levelIndex = 0
        while level:
            # check the order
            for i in range(1,len(level)):
                if levelIndex%2==0:
                    if level[i-1].val>=level[i].val:
                        return False
                else:
                    if level[i-1].val<=level[i].val:
                        return False
                    
            tmp = level[::]
            level.clear()
            for node in tmp:
                # check even or odd
                if node.val%2 == levelIndex%2:
                    return False
                
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            levelIndex += 1
        return True