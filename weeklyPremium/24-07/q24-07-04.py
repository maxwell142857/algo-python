from collections import defaultdict
import heapq as h
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(list)
        for c1,c2,cost in highways:
            graph[c1].append([cost,c2])
            graph[c2].append([cost,c1])
        # dp[i][j],the cost of from city0 to cityi with j discount used
        dp = [[-1]*(discounts+1) for _ in range(n)]
        for i in range(discounts+1):
            dp[0][i] = 0
        
        # run djistra
        heap = [] # [cost,city,discount used]
        for neighbor in graph[0]:
           h.heappush(heap,[neighbor[0],neighbor[1],0])
           if discounts > 0:
               h.heappush(heap,[neighbor[0]//2,neighbor[1],1])
        while heap:
            val,c,cnt = h.heappop(heap)
            if dp[c][cnt] != -1:
                continue
            else:
                dp[c][cnt] = val
                for neighbor in graph[c]:
                    if dp[neighbor[1]][cnt] == -1:
                        h.heappush(heap,[val+neighbor[0],neighbor[1],cnt])
                    if cnt < discounts:
                        if dp[neighbor[1]][cnt+1] == -1:
                            h.heappush(heap,[val+neighbor[0]//2,neighbor[1],cnt+1])

        ans = dp[n-1][0]
        for i in range(1,discounts+1):
            if dp[n-1][i] < 0:
                return ans
            else:
                ans = min(ans,dp[n-1][i])
        return ans
        