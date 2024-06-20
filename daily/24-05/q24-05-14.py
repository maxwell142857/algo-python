class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])
        ans = 0
        visited = set()
        def DFS(r,c,val):
            nonlocal ans

            val += grid[r][c]
            ans = max(ans,val)
            rr = [0,0,-1,1]
            cc = [-1,1,0,0]
            for i in range(4):
                newR = r+rr[i]
                newC = c+cc[i]
                if 0<=newR<rowCnt and 0<=newC<colCnt and (newR,newC) not in visited and grid[r][c] != 0:
                    visited.add((newR,newC))
                    DFS(newR,newC,val)
                    visited.remove((newR,newC))
        
        for i in range(rowCnt):
            for j in range(colCnt):
                if grid[i][j] != 0:
                    visited = set()
                    visited.add((i,j))
                    DFS(i,j,0)
                    visited.remove((i,j))
        return ans
