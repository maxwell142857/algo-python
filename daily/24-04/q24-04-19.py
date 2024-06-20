class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])
        visited = set()
        bias = [(1,0),(0,1),(-1,0),(0,-1)]
        def DFS(r,c):
            visited.add((r,c))
            for i in range(4):
                rr = r+bias[i][0]
                cc = c+bias[i][1]
                if 0<=rr<rowCnt and 0<=cc<colCnt and (rr,cc) not in visited and grid[rr][cc] == '1':
                    DFS(rr,cc)
        
        cnt = 0
        for i in range(rowCnt):
            for j in range(colCnt):
                if (i,j) not in visited and grid[i][j] == '1':
                    DFS(i,j)
                    cnt += 1
        return cnt