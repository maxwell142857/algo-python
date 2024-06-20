from collections import deque


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {} # key-value: name-edgeValue
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        map = {} # key-value: name-node

        equationsCnt = len(equations)
        for i in range(equationsCnt):
            a,b = equations[i]
            if a not in map:
                map[a] = Node(a)
            if b not in map:
                map[b] = Node(b)
            map[a].neighbors[b] = values[i]
            map[b].neighbors[a] = 1/values[i]

        ans = []
        for query in queries:
            if query[0] not in map or query[1] not in map:
                ans.append(-1.0)
                continue
            tmp = -1.0
            start = map[query[0]]

            queue = deque()
            queue.append([start,1])
            visited = set()
            visited.add(query[0])
            while len(queue) != 0:
                current = queue.popleft()
                for key in current[0].neighbors.keys():
                    if key == query[1]:
                        # find the ans
                        tmp = current[1]*current[0].neighbors[key]
                        break

                    if key not in visited:
                        queue.append([map[key],current[1]*current[0].neighbors[key]])
                        visited.add(key)

            ans.append(tmp)
        return ans