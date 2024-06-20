# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # traverse whole tree
    # def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    #     preVal = float("inf")
    #     find = None
    #     def traverse(node):
    #         nonlocal preVal,find
            
    #         if node.left:
    #             traverse(node.left)
    #         if preVal == p.val:
    #             find = node
    #         preVal = node.val
    #         if node.right:
    #             traverse(node.right)
        
    #     traverse(root)
    #     return find
    
    # use BST property
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        pointer = root
        while pointer:
            if pointer.val <= p.val:
                pointer = pointer.right
            else:
                successor = pointer
                pointer = pointer.left
        return successor
        
                
            