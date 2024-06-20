from collections import defaultdict
import heapq as h
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a,b,c in times:
            graph[a].append((b,c))
        minHeap = [(0,k)]
        visited = set()
        while minHeap:
            dis,cur = h.heappop(minHeap)
            if cur not in visited:
                visited.add(cur)
                if len(visited) == n:
                    return dis
                
                for neighbor,cost in graph[cur]:
                    h.heappush(minHeap,(dis+cost,neighbor))
        return -1
