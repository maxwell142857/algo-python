import heapq as h
class Solution:
    # O(V*(V+E)*logV),run djstra for each start
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph= defaultdict(list)
        for a,b,c in roads:
            graph[a].append((b,c))
            graph[b].append((a,c))
        
        result = []
        for start in range(1,n+1):
            distance = [float('inf')]*(n+1)
            ans = float('inf')
            minHeap = [(0,start)]
            while minHeap:
                dis,node = h.heappop(minHeap)
                if distance[node] == float('inf'):
                    distance[node] = dis
                    ans = min(ans,dis*(k+1)+appleCost[node-1])
                    for neighbor,cost in graph[node]:
                        h.heappush(minHeap,(dis+cost,neighbor))
            result.append(ans)
        return result
        