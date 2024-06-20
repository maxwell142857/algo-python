# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict,deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        # convert tree to graph
        graph = defaultdict(list)
        
        def convert(node):
            val = node.val
            if node.left:
                graph[val].append(node.left.val)
                graph[node.left.val].append(val)
                convert(node.left)
            if node.right:
                graph[val].append(node.right.val)
                graph[node.right.val].append(val)
                convert(node.right)
        
        convert(root)
        # BFS to find ans 
        level = deque()
        level.append(target.val)
        step = 0
        visited = set()
        visited.add(target.val)
        while level:
            l = len(level)
            for _ in range(l):
                cur = level.popleft()
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        level.append(neighbor)
            step += 1
            if step == k:
                return list(level)
        return []
