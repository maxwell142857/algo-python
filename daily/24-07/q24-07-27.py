import heapq as h
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[-1]*26 for _ in range(26)]
        edgeCnt = len(original)
        for i in range(edgeCnt):
            fromIndex = ord(original[i])-ord('a')
            toIndex = ord(changed[i])-ord('a')
            if graph[fromIndex][toIndex] == -1:
                graph[fromIndex][toIndex] = cost[i]
            else:
                graph[fromIndex][toIndex] = min(graph[fromIndex][toIndex],cost[i])
        # run djstra for each char
        minCost = [[-1]*26 for _ in range(26)]
        for i in range(26):
            heap = []
            minCost[i][i] = 0
            for j in range(26):
                if graph[i][j] != -1:
                    h.heappush(heap,[graph[i][j],j])
            while heap:
                val,node = h.heappop(heap)
                if minCost[i][node] != -1:
                    continue
                else:
                    minCost[i][node] = val
                    for j in range(26):
                        if graph[node][j] != -1 and minCost[i][j] == -1:
                            h.heappush(heap,[graph[node][j]+val,j])
        
        # calculate ans
        ans = 0
        n = len(source)
        for i in range(n):
            fromIndex = ord(source[i])-ord('a')
            toIndex = ord(target[i])-ord('a')
            if minCost[fromIndex][toIndex] == -1:
                return -1
            else:
                ans += minCost[fromIndex][toIndex]
        return ans