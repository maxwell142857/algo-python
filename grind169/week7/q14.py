# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        result = []
        fromLeft = True
        while level:
            ans = []
            tmp = level[:]
            if fromLeft:
                for node in level:
                    ans.append(node.val)
            else:
                level = level[::-1]
                for node in level:
                    ans.append(node.val)
            result.append(ans)
            fromLeft = not fromLeft
            level.clear()
            for node in tmp:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        return result

