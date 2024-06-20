# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        rightPointer = root
        
        leftPart = root.left
        rightPart = root.right
        root.left = None
        root.right = None

        def DFS(root):
            nonlocal rightPointer
            if not root:
                return
            leftPart = root.left
            rightPart = root.right
            root.left = None
            root.right = None

            rightPointer.right = root
            rightPointer = rightPointer.right

            DFS(leftPart)
            DFS(rightPart)
        
        DFS(leftPart)
        DFS(rightPart)

        return root