# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)
        def check(node,fatherAlive):
            if not node:
                return
            
            left,right = node.left,node.right
            
            if left and left.val in to_delete:
                node.left = None
            if right and right.val in to_delete:
                node.right = None
            
            if node.val in to_delete:
                node.left = None
                node.right = None
                check(left,False)
                check(right,False)
            else:
                if not fatherAlive:
                    result.append(node)
                check(left,True)
                check(right,True)
            
            

        check(root,False)
        return result
    
    # postorder traversal
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)

        def processNode(node):
            if not node:
                return None
            
            left = processNode(node.left)
            right = processNode(node.right)

            if node.val in to_delete:
                node.left = None
                node.right = None
                if left:
                    result.append(left)
                if right:
                    result.append(right)
                return None
            else:
                node.left = left
                node.right = right
                return node
        
        root = processNode(root)
        if root:
            result.append(root)
        return result
    
    # BFS
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        queue = deque()
        result = []
        to_delete = set(to_delete)
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            
            # update the result
            if cur.val in to_delete:
                if cur.left and cur.left.val not in to_delete:
                    result.append(cur.left)
                if cur.right and cur.right.val not in to_delete:
                    result.append(cur.right)

            # delete connections between parent and son
            if cur.val in to_delete:
                cur.left = None
                cur.right = None
            if cur.left and cur.left.val in to_delete:
                cur.left = None
            if cur.right and cur.right.val in to_delete:
                cur.right = None
            
            

        if root.val not in to_delete:
            result.append(root)
        return result




