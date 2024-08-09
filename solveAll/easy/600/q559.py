from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                cur = queue.popleft()
                for son in cur.children:
                    queue.append(son)
            level += 1
        return level
