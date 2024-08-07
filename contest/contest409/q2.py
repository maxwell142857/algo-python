from collections import defaultdict,deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(n-1):
            graph[i].append(i+1)
        ans = []

        def BFS():
            visited = set()
            level = deque()
            level.append(0)
            distance = 0
            while level:
                l = len(level)
                for _ in range(l):
                    cur = level.popleft()
                    if cur == n-1:
                        return distance
                    for son in graph[cur]:
                        if son not in visited:
                            level.append(son)
                            visited.add(son)
                distance += 1
            return -1
        
        for a,b in queries:
            graph[a].append(b)
            ans.append(BFS())
        return ans
