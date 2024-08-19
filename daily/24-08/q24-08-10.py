class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # build the map
        rowCnt = len(grid)
        colCnt = len(grid[0])
        map = [[0]*(3*colCnt) for _ in range(3*rowCnt)]
        for r in range(rowCnt):
            for c in range(colCnt):
                if grid[r][c] == '/':
                    map[3*r][3*c+2] = 1
                    map[3*r+1][3*c+1] = 1
                    map[3*r+2][3*c] = 1
                elif grid[r][c] == '\\':
                    map[3*r][3*c] = 1
                    map[3*r+1][3*c+1] = 1
                    map[3*r+2][3*c+2] = 1
        rowCnt *= 3
        colCnt *= 3

        # run dfs
        def DFS(r,c):
            visited[r][c] = True
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for i in range(4):
                rr = r+directions[i][0]
                cc = c+directions[i][1]
                if 0<=rr<rowCnt and 0<=cc<colCnt and map[rr][cc] == 0 and not visited[rr][cc]:
                    DFS(rr,cc)
        
        visited = [[False]*(colCnt) for _ in range(rowCnt)]
        ans = 0
        for r in range(rowCnt):
            for c in range(colCnt):
                if map[r][c]==0 and not visited[r][c]:
                    DFS(r,c)
                    ans += 1
        return ans