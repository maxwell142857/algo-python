class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])
        
        for i in range(rowCnt):
            if grid[i][0] == 0:
                for j in range(colCnt):
                    grid[i][j] = (grid[i][j]+1)%2
        
        total = 0 
        val = 2**(colCnt-1)
        for j in range(colCnt):
            cnt = 0
            for i in range(rowCnt):
                if grid[i][j] == 1:
                    cnt += 1
            total += val*max(cnt,rowCnt-cnt)
            val >>= 1
        return total
            
