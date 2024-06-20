import heapq
class Solution:
    # O(n^3), dp
    # def minFallingPathSum(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     dp = [[0]*n for _ in range(n)]
    #     for i in range(n):
    #         dp[0][i] = grid[0][i]
        
    #     for i in range(1,n):
    #         for j in range(n):
    #             # calculate dp[i][j] based on dp[i-1][:]
    #             lastMin = float('inf')
    #             for k in range(n):
    #                 if k == j:
    #                     continue
    #                 lastMin = min(lastMin,dp[i-1][k])
    #             dp[i][j] = lastMin+grid[i][j]

    #     return min(dp[n-1])
    
    # O(n^2),dp with optimization

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0]*n for _ in range(n)]
        maxHeap = []
        for i in range(n):
            dp[0][i] = grid[0][i]
            heapq.heappush(maxHeap,(-grid[0][i],i))
            if len(maxHeap) == 3:
                heapq.heappop(maxHeap)
        
        for i in range(1,n):
            first = maxHeap[1]
            second = maxHeap[0]
            maxHeap = []
            for j in range(n):
                # calculate dp[i][j] based on dp[i-1][:]
                if j != first[1]:
                    dp[i][j] = -first[0]+grid[i][j]
                else:
                    dp[i][j] = -second[0]+grid[i][j]
                heapq.heappush(maxHeap,(-dp[i][j],j))
                if len(maxHeap) == 3:
                    heapq.heappop(maxHeap)

        return min(dp[n-1])
