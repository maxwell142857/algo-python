from collections import defaultdict,deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        inDegree = [0]*n
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            inDegree[b] += 1
        
        queue = deque()
        for i in range(n):
            if inDegree[i] == 0:
                queue.append(i)
        
        while queue:
            l = len(queue)
            for _ in range(l):
                cur = queue.popleft()
                for son in graph[cur]:
                    ans[son] |= ans[cur]
                    ans[son].add(cur)
                    inDegree[son] -= 1
                    if inDegree[son] == 0:
                        queue.append(son)
        result = [list(a) for a in ans]
        for r in result:
            r.sort()
        return result