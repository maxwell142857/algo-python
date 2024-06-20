class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*n for _ in range(2)]
        for level in range(n):
            dp[level%2][0] = dp[(level+1)%2][0]+triangle[level][0]
            for index in range(1,level):
                dp[level%2][index] = min(dp[(level+1)%2][index],dp[(level+1)%2][index-1])+triangle[level][index]
            dp[level%2][level] = dp[(level+1)%2][level-1]+triangle[level][level]
        return min(dp[(n-1)%2])
