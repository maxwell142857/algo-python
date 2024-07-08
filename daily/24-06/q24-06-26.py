# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        array = []
        self.inOrderTraverse(root,array)
        return self.buildBST(0,len(array)-1,array)

    def inOrderTraverse(self,node,array):
        if not node:
            return
        
        self.inOrderTraverse(node.left,array)
        array.append(node.val)
        self.inOrderTraverse(node.right,array)
    
    # build range: array[left:right+1]
    def buildBST(self,left,right,array):
        if left == right:
            return TreeNode(array[left])
        if left>right:
            return None
        
        mid = (left+right)//2
        cur = TreeNode(array[mid])
        cur.left = self.buildBST(left,mid-1,array)
        cur.right = self.buildBST(mid+1,right,array)
        return cur
