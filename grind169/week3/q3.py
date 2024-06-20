
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        number2Node = {}
        update = set()
        queue = deque()
        queue.append(node)
        update.add(node.val)
        startVal = node.val
        while queue:
            tmp = queue.popleft()
            if tmp.val in number2Node:
                newOne = number2Node[tmp.val]
            else:
                newOne = Node(tmp.val)
                number2Node[tmp.val] = newOne

            for son in tmp.neighbors:
                if son.val not in update:
                    queue.append(son)
                    update.add(son.val)
                if son.val not in number2Node:
                    newSon = Node(son.val)
                    number2Node[son.val] = newSon
                    newOne.neighbors.append(newSon)
                else:
                    newOne.neighbors.append(number2Node[son.val])
        return number2Node[startVal]