class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])

        top = 0
        for r in range(rowCnt):
            for c in range(colCnt):
                if grid[r][c] != 0:
                    top += 1

        front = 0
        for row in grid:
            front += max(row)
        
        side = 0
        for c in range(colCnt):
            val = grid[0][c]
            for r in range(1,rowCnt):
                val = max(val,grid[r][c])
            side += val
        
        return top+front+side
        