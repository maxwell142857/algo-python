class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftH = [0]*n
        for i in range(1,n):
            leftH[i] = max(leftH[i-1],height[i-1])
        rightH = [0]*n
        for i in range(n-2,-1,-1):
            rightH[i] = max(rightH[i+1],height[i+1])
        ans = 0
        for i in range(1,n-1):
            col = min(leftH[i],rightH[i])
            if col - height[i] > 0:
                ans += col - height[i]
        return ans
        