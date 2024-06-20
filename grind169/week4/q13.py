class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        prePointer = 0

        def build(start,end):
            nonlocal prePointer
            if start > end:
                return None
            
            p = start
            while inorder[p] != preorder[prePointer]:
                p += 1
            node = TreeNode(preorder[prePointer])
            prePointer += 1
            node.left = build(start,p-1)
            node.right = build(p+1,end)
            return node

        root = build(0,len(inorder)-1)
        return root