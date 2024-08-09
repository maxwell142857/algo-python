# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def DFS(cur,path):
            if not cur.left and not cur.right:
                ans.append('->'.join(path))
                return
            if cur.left:
                path.append(str(cur.left.val))
                DFS(cur.left,path)
                path.pop()
            if cur.right:
                path.append(str(cur.right.val))
                DFS(cur.right,path)
                path.pop()

        path = [str(root.val)]
        DFS(root,path)
        return ans
