class Solution:
    # simulation: O(n^2)
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for i in range(0,n):
            for j in range(i+1,n):
                tmp = min(height[i],height[j])*(j-i)
                ans = max(ans,tmp)
        return ans
    # two pointer:O(n)
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left = 0
        right = n-1
        while left < right:
            tmp = min(height[left],height[right])*(right-left)
            ans = max(ans,tmp)
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
        return ans
    
