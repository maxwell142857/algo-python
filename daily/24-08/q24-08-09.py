class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(r,c):
            # check rows
            for i in range(r-1,r+2):
                val = 0
                for j in range(c-1,c+2):
                    val += grid[i][j]
                if val != 15:
                    return False
            # check row
            for j in range(c-1,c+2):
                val = 0
                for i in range(r-1,r+2):
                    val += grid[i][j]
                if val != 15:
                    return False
            # check diagonals
            if grid[r-1][c-1]+grid[r+1][c+1] != grid[r-1][c+1]+grid[r+1][c-1]:
                return False
            # check distinct
            used = set(range(1,10))
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if grid[i][j] in used:
                        used.remove(grid[i][j])
                    else:
                        return False
            
            return True
        cnt = 0
        rowCnt = len(grid)
        colCnt = len(grid[0])
        for r in range(1,rowCnt-1):
            for c in range(1,colCnt-1):
                if check(r,c):
                    cnt += 1
        return cnt