class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def countIsland(map):
            rowCnt = len(map)
            colCnt = len(map[0])
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            def DFS(r,c,visited):
                visited[r][c] = True
                for i in range(4):
                    rr = r+directions[i][0]
                    cc = c+directions[i][1]
                    if 0<=rr<rowCnt and 0<=cc<colCnt and map[rr][cc] == 1 and not visited[rr][cc]:
                        DFS(rr,cc,visited)
        
            # run dfs to get island cnt on origin land
            visited = [[False]*colCnt for _ in range(rowCnt)]
            cnt = 0
            for r in range(rowCnt):
                for c in range(colCnt):
                    if map[r][c] == 1 and not visited[r][c]:
                        DFS(r,c,visited)
                        cnt += 1
            return cnt
        
        originCnt = countIsland(grid)
        if originCnt != 1:
            return 0
        
        # check whether we can only delete one island
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    result = countIsland(grid)
                    grid[r][c] = 1
                    if result != 1:
                        return 1
        # we can not only delete one island
        return 2

        



        