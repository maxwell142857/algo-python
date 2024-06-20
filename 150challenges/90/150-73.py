# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postIndex = len(postorder)-1
        val2index = {x:i for i,x in enumerate(inorder)}
        def construct(inorderStart,inorderEnd):
            if inorderEnd<inorderStart:
                return None
            
            nonlocal postIndex
            root = TreeNode(postorder[postIndex])
            postIndex -= 1
            if inorderStart == inorderEnd:
                return root
            else:
                spliteIndex = val2index[root.val]
                root.right = construct(spliteIndex+1,inorderEnd)
                root.left = construct(inorderStart,spliteIndex-1)
                return root
        
        return construct(0,len(inorder)-1)

    