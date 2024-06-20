# Given the root of a binary tree, return the vertical order traversal of its nodes' values. 
# (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.



# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        col2nodes = {}

        def DFS(node,col):
            if col in col2nodes:
                col2nodes[col].append(node.val)
            else:
                col2nodes[col] = [node.val]
            if node.left:
                DFS(node.left,col-1)
            if node.right:
                DFS(node.right,col+1)
            
        DFS(root,0)
        tmp = []
        for key,val in col2nodes.items():
            tmp.append((key,val))
        tmp.sort()
        ans = []
        for line in tmp:
            ans.append(line[1])
        return ans
    
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        col2nodes = {}

        mydeque = deque()
        mydeque.append((0,root))

        while mydeque:
            node = mydeque.popleft()
            colID = node[0]
            if colID in col2nodes:
                col2nodes[colID].append(node[1].val)
            else:
                col2nodes[colID] = [node[1].val]
            
            if node[1].left:
                mydeque.append((colID-1,node[1].left))
            if node[1].right:
                mydeque.append((colID+1,node[1].right))

        tmp = []
        for key,val in col2nodes.items():
            tmp.append((key,val))
        tmp.sort() 
        ans = []
        for line in tmp:
            ans.append(line[1])
        return ans
    
    # n+m*log(m)
    # n*log(n)

