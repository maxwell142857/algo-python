class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[] for _ in range(n-2)]
        for i in range(1,n-1):
            for j in range(1,n-1):
                # caculate maxVal in 3*3 center in grid[i][j]
                maxVal = grid[i][j]
                for k in range(-1,2):
                    maxVal = max(maxVal,max(grid[i+k][j-1:j+2]))
                result[i-1].append(maxVal)
        return result