import heapq as h
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph =defaultdict(list)
        for a,b,c in edges:
            graph[a].append((c,b))
            graph[b].append((c,a))
        

        ans = [0]*n
        for i in range(n):
            heap = []
            distance = [-1]*n
            distance[i] = 0
            for son in graph[i]:
                h.heappush(heap,[son[0],son[1]])
            while heap:
                val,to = h.heappop(heap)
                if val > distanceThreshold:
                    break
                if distance[to] != -1:
                    continue
                distance[to] = val
                for son in graph[to]:
                    if distance[son[1]] == -1:
                        h.heappush(heap,[son[0]+val,son[1]])
            for i in range(n):
                if distance[i] != -1:
                    ans[i] += 1
        minVal = min(ans)
        for i in range(n-1,-1,-1):
            if ans[i] == minVal:
                return i
        return -1

            

            
