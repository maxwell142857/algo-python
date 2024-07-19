# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # find the Lowest Common Ancestor (LCA), then find start to LAC, LAC to dest
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent = None

        def findParent(cur):
            nonlocal parent
            if not cur:
                return 0
            
            cnt = 0
            if cur.val == startValue or cur.val == destValue:
                cnt += 1
            cnt += findParent(cur.left)
            cnt += findParent(cur.right)
            if cnt == 2:
                parent = cur
                return -1
            else:
                return cnt
        
        findParent(root)

        # calculate distance from parent to startPoint

        queue = deque()
        queue.append(parent)
        levelCnt = 0
        find = False
        while queue:
            l = len(queue)
            for _ in range(l):
                cur = queue.popleft()
                if cur.val == startValue:
                    find = True
                    break
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if find:
                break
            levelCnt += 1
        
        # find path from parent to destPoint
        path2dest = None
        path = []
        def traverse(cur):
            nonlocal path2dest
            if not cur:
                return 
            
            if cur.val == destValue:
                path2dest = ''.join(path)
                return
            
            path.append('L')
            traverse(cur.left)
            path.pop()

            path.append('R')
            traverse(cur.right)    
            path.pop()  
        traverse(parent)

        # combine two path together
        return 'U'*levelCnt+path2dest

        
            
    # similar as previous, optimized
    # do not find LAC, just find root to start, root to dest, then intersect    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(node,target,path):
            if not node:
                return False
            
            if node.val == target:
                return True
            
            path.append('L')
            if findPath(node.left,target,path):
                return True
            path.pop()

            path.append('R')
            if findPath(node.right,target,path):
                return True
            path.pop()

            return False

        path2start,path2end = [],[]
        findPath(root,startValue,path2start)
        findPath(root,destValue,path2end)

        p = 0
        while p < len(path2start) and p < len(path2end) and path2start[p]==path2end[p]:
            p += 1
        return 'U'*(len(path2start)-p)+''.join(path2end[p:])

