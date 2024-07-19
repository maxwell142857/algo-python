"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return []

        def traverse(node):
            
            for son in node.children:
                traverse(son)
            
            result.append(node.val)

        traverse(root)
        return result