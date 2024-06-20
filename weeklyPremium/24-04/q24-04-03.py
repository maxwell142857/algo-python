# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def areYouLonely(node):
            if node.left and node.right:
                areYouLonely(node.left)
                areYouLonely(node.right)
            elif node.left:
                areYouLonely(node.left)
                ans.append(node.left.val)
            elif node.right:
                areYouLonely(node.right)
                ans.append(node.right.val)
        
        areYouLonely(root)
        return ans