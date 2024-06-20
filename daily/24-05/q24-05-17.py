# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def deleteNode(cur):
            if not cur:
                return None
            
            cur.left = deleteNode(cur.left)
            cur.right = deleteNode(cur.right)

            if not cur.left and not cur.right and cur.val == target:
                return None
            else:
                return cur
        
        return deleteNode(root)