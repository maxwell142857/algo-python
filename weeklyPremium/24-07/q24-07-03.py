# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        ans = -1
        # return p or q'distance to this node
        # if can not find, return -1
        def process(node):
            nonlocal ans
            if not node or ans != -1:
                return -1
            
            left = process(node.left)
            right = process(node.right)
            if left==-1 and right==-1:
                if node.val==p or node.val==q:
                    return 0
                else:
                    return -1
            elif left == -1:
                if node.val==p or node.val==q:
                    ans = right+1
                    return -1
                else:
                    return right+1
            elif right == -1:
                if node.val==p or node.val==q:
                    ans = left+1
                    return -1
                else:
                    return left+1
            else:
                ans = left+right+2
                return -1
        if p == q:
            return 0
        process(root)
        return ans

