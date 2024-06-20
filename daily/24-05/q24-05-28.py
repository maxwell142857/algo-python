class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = [abs(ord(s[i])-ord(t[i])) for i in range(n)]
        left = 0
        curSum = 0
        l = 0
        for right in range(n):
            curSum += diff[right]
            while left<=right and curSum>maxCost:
                curSum -= diff[left]
                left += 1
            l = max(l,right-left+1)
        return l
