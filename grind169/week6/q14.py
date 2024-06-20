# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        root.val = 0
        level = [(root,1)]
        while level:
            if len(level)>=2:
                ans = max(ans,level[-1][1]-level[0][1]+1)

            tmp = []
            for node in level:
                if node[0].left:
                    tmp.append((node[0].left,node[1]*2))
                if node[0].right:
                    tmp.append((node[0].right,node[1]*2+1))
            level = tmp
        return ans