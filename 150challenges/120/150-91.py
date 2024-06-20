
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start = Node(node.val)
        hashmap = {}
        hashmap[node.val] = start
        
        visited = set()
        visited.add(node.val)
        
        queue = deque()
        queue.append(node)

        while len(queue) != 0:
            current = queue.popleft()
            
            if current.val in hashmap:
                copy = hashmap[current.val]
            else:
                copy = Node(current.val)
                hashmap[current.val] = copy
            for neighbor in current.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor.val)

                if neighbor.val in hashmap:
                    copy.neighbors.append(hashmap[neighbor.val])
                else:
                    newNode = Node(neighbor.val)
                    hashmap[neighbor.val] = newNode
                    copy.neighbors.append(newNode)
            
            
        return start
                