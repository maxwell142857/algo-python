class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        used = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0

        def DFS(indexI,indexJ):
            nonlocal m,n
            if grid[indexI][indexJ] == '1' and used[indexI][indexJ] ==0:
                used[indexI][indexJ] = 1
                if indexI-1 >= 0 :
                    DFS(indexI-1,indexJ)
                if indexI+1 < m:
                    DFS(indexI+1,indexJ)
                if indexJ-1 >= 0:
                    DFS(indexI,indexJ-1)
                if indexJ+1 < n:
                    DFS(indexI,indexJ+1)
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and used[i][j] ==0:
                    DFS(i,j)
                    ans += 1
        return ans 