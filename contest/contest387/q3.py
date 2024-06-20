from collections import defaultdict


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        Y = defaultdict(int)

        # diagonal
        for i in range(n//2+1):
            number = grid[i][i]
            Y[number] += 1
        print(Y)
        # anti-diagnal
        for i in range(n//2):
            number = grid[i][n-i-1]
            Y[number] += 1
        print(Y)
        # vertical
        for i in range(n//2+1,n):
            number = grid[i][n//2]
            Y[number] += 1
        print(Y)
        

        remain = defaultdict(int)
        for i in range(n):
            for j in range(n):
                number = grid[i][j]
                remain[number] += 1
        remain[0] -= Y[0]
        remain[1] -= Y[1]
        remain[2] -= Y[2]
        
        YCnt = Y[0]+Y[1]+Y[2]
        remainCnt = n**2-YCnt
        ans = n**2
        # emunate (remain,Y) as (0,1) (0,2) (1,0) (1,2) (2,0) (2,1)
        ans = min(ans,remainCnt-remain[0]+YCnt-Y[1])
        ans = min(ans,remainCnt-remain[0]+YCnt-Y[2])
        ans = min(ans,remainCnt-remain[1]+YCnt-Y[0])
        ans = min(ans,remainCnt-remain[1]+YCnt-Y[2])
        ans = min(ans,remainCnt-remain[2]+YCnt-Y[0])
        ans = min(ans,remainCnt-remain[2]+YCnt-Y[1])
        return ans
# [[0,1,0],[2,1,0],[0,2,0]]