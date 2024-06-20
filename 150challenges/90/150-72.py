# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndex = 0

        def construct(preorder,inorder):
            if len(inorder) == 0:
                return None
            nonlocal preIndex
            root = TreeNode(preorder[preIndex])
            preIndex += 1
            if len(inorder) == 1:
                return root
            else:
                for i in range(len(inorder)):
                    if inorder[i] == root.val:
                        root.left = construct(preorder,inorder[:i])
                        root.right = construct(preorder,inorder[i+1:])
                        break
                return root
        
        return construct(preorder,inorder)
    
# more elegant
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndex = 0
        val2index = {x:i for i,x in enumerate(inorder)}
        def construct(inorderStart,inorderEnd):
            if inorderEnd<inorderStart:
                return None
            
            nonlocal preIndex
            root = TreeNode(preorder[preIndex])
            preIndex += 1
            if inorderStart == inorderEnd:
                return root
            else:
                spliteIndex = val2index[root.val]
                root.left = construct(inorderStart,spliteIndex-1)
                root.right = construct(spliteIndex+1,inorderEnd)
                return root
        
        return construct(0,len(inorder)-1)

        

        