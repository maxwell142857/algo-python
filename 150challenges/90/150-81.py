class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = -1
        def find(node):
            nonlocal ans 
            if not node:
                return False
            left = find(node.left)
            right = find(node.right)
            if node==p or node==q:
                if left or right:
                    ans = node
                    return False # already find answer, prevent new ans
                else:
                    return True 
            else:
                if left and right:
                    ans = node
                    return False # already find answer, prevent new ans
                else:
                    return left or right
                
        find(root)
        return ans
            
s = Solution()
root = TreeNode(1)
left = TreeNode(2)
root.left = left
print(s.lowestCommonAncestor(root,root,left))