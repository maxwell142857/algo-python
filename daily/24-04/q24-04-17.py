# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        path = []
        ans = None
        def num2c(list):
            res = ''
            for i in range(len(list)):
                res += chr(ord('a')+list[i])
            return res
        
        def DFS(node):
            nonlocal ans
            if not node.left and not node.right:
                s = num2c(path[::-1])
                if not ans or ans > s:
                    ans = s
                return
            if node.left:
                path.append(node.left.val)
                DFS(node.left)
                path.pop()
            if node.right:
                path.append(node.right.val)
                DFS(node.right)
                path.pop()

        path.append(root.val)
        DFS(root)
        return ans
