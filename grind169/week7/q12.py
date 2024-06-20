class Solution:
    # O(m^2*n), fix length(min value of m,n),and do dp
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     rowCnt = len(matrix)
    #     colCnt = len(matrix[0])
    #     length = min(rowCnt,colCnt)
    #     pre = [[False]*colCnt for _ in range(rowCnt)]
    #     ans = 0
    #     for i in range(rowCnt):
    #         for j in range(colCnt):
    #             if matrix[i][j] == '1':
    #                 pre[i][j] = True
    #                 ans = 1

    #     for l in range(2,length+1):
    #         cur = [[False]*colCnt for _ in range(rowCnt)]
    #         find = False
    #         for i in range(rowCnt):
    #             for j in range(colCnt):
    #                 if i+l-1<rowCnt and j+l-1<colCnt and pre[i][j] and pre[i+1][j+1] and matrix[i+l-1][j] == '1' and matrix[i][j+l-1] == '1':
    #                     cur[i][j] = True
    #                     ans = l
    #         pre = cur
    #     return ans**2
    
    # O(n*m) standard dp
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        dp = [[0]*(colCnt+1) for _ in range(rowCnt+1)]
        l = 0
        for i in range(1,rowCnt+1):
            for j in range(1,colCnt+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    l = max(l,dp[i][j])
        return l*l
