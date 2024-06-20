class Solution:
    # DFS on each point
    # O(mn*2^(mn)), since DFS is O(V+E),here E is 2^V
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     rowCnt = len(matrix)
    #     colCnt = len(matrix[0])

    #     l = 1
    #     def DFS(r,c,val):
    #         nonlocal l
    #         bias = [[0,1],[1,0],[0,-1],[-1,0]]
    #         for i in range(4):
    #             rr = r+bias[i][0]
    #             cc = c+bias[i][1]
    #             if 0<=rr<rowCnt and 0<=cc<colCnt and matrix[rr][cc] >matrix[r][c]:
    #                 l = max(l,val+1)
    #                 DFS(rr,cc,val+1)
        
    #     for i in range(rowCnt):
    #         for j in range(colCnt):
    #             DFS(i,j,1)
    #     return l

    # DFS with memo
    # O(mn)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        memo = [[-1]*colCnt for _ in range(rowCnt)]

        def DFS(r,c):
            if memo[r][c] != -1:
                return memo[r][c]
            
            l = 0
            bias = [[0,1],[1,0],[0,-1],[-1,0]]
            for i in range(4):
                rr = r+bias[i][0]
                cc = c+bias[i][1]
                if 0<=rr<rowCnt and 0<=cc<colCnt and matrix[rr][cc] >matrix[r][c]:
                    l = max(l,DFS(rr,cc))

            memo[r][c] = l+1
            return memo[r][c]
        ans = 0
        for i in range(rowCnt):
            for j in range(colCnt):
                DFS(i,j)
                ans = max(ans,memo[i][j])

        return ans
