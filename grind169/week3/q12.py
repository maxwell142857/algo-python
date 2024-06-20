class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])
        level = []
        totalCnt = 0
        time = 0
        for i in range(rowCnt):
            for j in range(colCnt):
                if grid[i][j] == 2:
                    level.append((i,j))
                if grid[i][j] == 1:
                    totalCnt += 1
        if totalCnt == 0:
            return 0
        
        c_ = [0,0,-1,1]
        r_ = [1,-1,0,0]
        while level:
            tmp = level[:]
            level = []
            for r,c in tmp:
                for i in range(4):
                    newR = r+r_[i]
                    newC = c+c_[i]
                    if 0<=newR<rowCnt and 0<=newC<colCnt and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        totalCnt -= 1
                        level.append((newR,newC))
            time += 1
            if totalCnt == 0:
                return time
        return -1
            
                    