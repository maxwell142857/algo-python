from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftHighest = [0]*n
        rightHighest = [0]*n
        for i in range(1,n):
            leftHighest[i] = max(leftHighest[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            rightHighest[i] = max(rightHighest[i+1],height[i+1])
        ans = 0
        for i in range(1,n-1):
            delta = min(leftHighest[i],rightHighest[i]) - height[i] 
            if delta > 0:
                ans += delta
                # print(f"Index:{i}, delta:{delta}")
        return ans
        
    
s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])