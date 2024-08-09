class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def calculate(r,c):
            if grid[r][c] == 0:
                return 0
            
            result = 2
            neighbor = [[1,0],[0,1],[-1,0],[0,-1]]
            for i in range(4):
                rr = r+neighbor[i][0]
                cc = c+neighbor[i][1]
                if 0<=rr<n and 0<=cc<n:
                    result += max(0,grid[r][c]-grid[rr][cc])
                else:
                    result += grid[r][c]
            return result
        
        ans = 0
        for r in range(n):
            for c in range(n):
                ans += calculate(r,c)
        return ans
