class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        firstLessIndex = [0]*n
        firstLessIndex[0] = -1
        for i in range(1,n):
            p = i-1 
            while heights[p]>=heights[i]:
                p = firstLessIndex[p]
                if p == -1:
                    break
            firstLessIndex[i] = p

        lastLessIndex = [0]*n
        lastLessIndex[-1] = n
        for i in range(n-2,-1,-1):
            p = i+1 
            while heights[p]>=heights[i]:
                p = lastLessIndex[p]
                if p == n:
                    break
            lastLessIndex[i] = p
 
        ans = 0
        for i in range(n):
            ans = max(ans,(lastLessIndex[i]-firstLessIndex[i]-1)*heights[i])
        return ans