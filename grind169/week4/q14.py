class Solution:
    # brute force n^2, TLE
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1,n):
                ans = max(ans,min(height[i],height[j])*(j-i))
        return ans
    # two pointer, O(n)
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        left = 0
        right = n-1
        while left < right:
            ans = max(ans,min(height[left],height[right])*(right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans