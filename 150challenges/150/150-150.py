class Solution:
    # O(n^3) recursion with memo, TLE
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = {}
        n = len(matrix)
        m = len(matrix[0])
        def check(start,end):
            if (start,end) in memo:
                return memo[(start,end)]
            ans = False
            if start == end:
                ans = matrix[start[0]][start[1]] == '1'
            else:
                halfL = (end[0]-start[0]+1)//2
                ans = check(start,(end[0]-halfL,end[1]-halfL)) and \
                check((start[0],start[1]+halfL),(end[0]-halfL,end[1])) and \
                check((start[0]+halfL,start[1]),(end[0],end[1]-halfL)) and \
                check((start[0]+halfL,start[1]+halfL),(end[0],end[1]))
            memo[(start,end)] = ans
            return ans 
                
        maxValue = 0
        for i in range(n):
            for j in range(m):
                for l in range(1,min(m,n)+1):
                    if i+l-1 >= n or j+l-1 >= m:
                        break

                    endI = i+l-1
                    endJ = j+l-1
                    result = check((i,j),(endI,endJ))
                    if result:
                        maxValue = max(maxValue,l)
        return maxValue**2
    
    # dp, O(n^2)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        length = 0
        
        for i in range(n):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                length = 1
        for j in range(m):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                length = 1

        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    length = max(length,dp[i][j])
        return length**2

                

