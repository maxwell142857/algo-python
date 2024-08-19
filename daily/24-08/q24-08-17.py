class Solution:
    # O(n*m)
    def maxPoints(self, points: List[List[int]]) -> int:
        rowCnt = len(points)
        colCnt = len(points[0])
        dp = [[0]*colCnt for _ in range(rowCnt)]
        dp[0] = points[0][:]
        for r in range(1,rowCnt):
            leftMax = [0]*colCnt
            leftMax[0] = dp[r-1][0]
            for c in range(1,colCnt):
                leftMax[c] = max(leftMax[c-1]-1,dp[r-1][c])
            
            rightMax = [0]*colCnt
            rightMax[colCnt-1] = dp[r-1][colCnt-1]
            for c in range(colCnt-2,-1,-1):
                rightMax[c] = max(rightMax[c+1]-1,dp[r-1][c])

            for c in range(colCnt):
                dp[r][c] = points[r][c]+max(leftMax[c],rightMax[c])

        return max(dp[rowCnt-1])

        