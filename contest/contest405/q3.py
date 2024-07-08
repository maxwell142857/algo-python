class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])
        dp = [[0]*colCnt for _ in range(rowCnt)] # record cnt(x)-cnt(y)
        isX = [[False]*colCnt for _ in range(rowCnt)]
        ans = 0

        def calculate(r,c):
            nonlocal ans
            tmp = 0 
            xFlag = False
            if r-1>=0:
                tmp += dp[r-1][c]
                xFlag |= isX[r-1][c]
            if c-1>=0:
                tmp += dp[r][c-1]
                xFlag |= isX[r][c-1]
            if r-1>=0 and c-1>=0:
                tmp -= dp[r-1][c-1]
            
            if grid[r][c] == 'X':
                tmp += 1
                xFlag = True
            elif grid[r][c] == 'Y':
                tmp -= 1

            dp[r][c] = tmp
            isX[r][c] = xFlag

            if tmp == 0 and xFlag:
                ans += 1
        
        for r in range(rowCnt):
            for c in range(colCnt):
                calculate(r,c)
        return ans
