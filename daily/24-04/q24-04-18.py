class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])
        def getVal(r,c):

            rr = [0,0,-1,1]
            cc = [1,-1,0,0]
            cnt = 4
            for i in range(4):
                newR = r+rr[i]
                newC = c+cc[i]
                if 0<=newR<rowCnt and 0<=newC<colCnt and grid[newR][newC] == 1:
                    cnt -= 1
            return cnt
        
        ans = 0
        for r in range(rowCnt):
            for c in range(colCnt):
                if grid[r][c] == 1:
                    ans += getVal(r,c)
        return ans
