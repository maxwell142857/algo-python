class Solution:
    # O(mn*max(m,n)), TLE
    # def maxScore(self, grid: List[List[int]]) -> int:
    #     rowCnt = len(grid)
    #     colCnt = len(grid[0])
    #     dp = [[float('-inf')]*colCnt for _ in range(rowCnt)]
    #     ans = float('-inf')

    #     for r in range(rowCnt):
    #         for c in range(colCnt):
    #             for pre in range(c):
    #                 if dp[r][pre]>0:
    #                     dp[r][c] = max(dp[r][c],dp[r][pre]+grid[r][c]-grid[r][pre])
    #                 else:
    #                     dp[r][c] = max(dp[r][c],grid[r][c]-grid[r][pre])
    #             for pre in range(r):
    #                 if dp[pre][c]>0:
    #                     dp[r][c] = max(dp[r][c],dp[pre][c]+grid[r][c]-grid[pre][c])
    #                 else:
    #                     dp[r][c] = max(dp[r][c],grid[r][c]-grid[pre][c])
    #             ans = max(ans,dp[r][c])
    #     return ans
    
    # O(mn)
    def maxScore(self, grid: List[List[int]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])

        minSquare = [[float('inf')]*colCnt for _ in range(rowCnt)]
        minSquare[0][0] = grid[0][0]
        for r in range(1,rowCnt):
            minSquare[r][0] = min(minSquare[r-1][0],grid[r][0])
        for c in range(1,colCnt):
            minSquare[0][c] = min(minSquare[0][c-1],grid[0][c])
        for r in range(1,rowCnt):
            for c in range(1,colCnt):
                minSquare[r][c] = min(minSquare[r-1][c],minSquare[r][c-1],grid[r][c])
        

        ans = float('-inf')
        for r in range(1,rowCnt):
            ans = max(ans,grid[r][0]-minSquare[r-1][0])
        for c in range(1,colCnt):
            ans = max(ans,grid[0][c]-minSquare[0][c-1])
        for r in range(1,rowCnt):
            for c in range(1,colCnt):
                ans = max(ans,grid[r][c]-minSquare[r][c-1],grid[r][c]-minSquare[r-1][c])
        return ans