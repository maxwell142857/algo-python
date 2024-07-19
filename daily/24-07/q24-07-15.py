# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        val2node = {}
        notRoot = set()
        for p,s,left in descriptions:
            if p not in val2node:
                val2node[p] = TreeNode(p)
            if s not in val2node:
                val2node[s] = TreeNode(s)
            
            if left:
                val2node[p].left = val2node[s]
            else:
                val2node[p].right = val2node[s]
            notRoot.add(s)

        for k in val2node.keys():
            if k not in notRoot:
                return val2node[k]