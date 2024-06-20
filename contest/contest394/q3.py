class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])
        dp = [[float('inf')]*colCnt for _ in range(10)]
        # dp[i][j] means the min cost of fill j-th col with val i
        # 0<=i<=9,0<=j<colCnt

        def fillCol(colIndex,val):
            cost = 0
            for i in range(rowCnt):
                if grid[i][colIndex] != val:
                    cost += 1
            return cost
        
        for i in range(0,10):
            dp[i][0] = fillCol(0,i)
        
        for j in range(1,colCnt):
            
            for i in range(0,10):
                colCost = fillCol(j,i)
                for pre in range(0,10):
                    if pre == i:
                        continue
                    dp[i][j] = min(dp[i][j],colCost+dp[pre][j-1])
        ans = float('inf')
        for i in range(0,10):
            ans = min(ans,dp[i][colCnt-1])
        
        return ans