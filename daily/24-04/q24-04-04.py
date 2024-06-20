class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        cnt = 0
        for c in s:
            if c =='(':
                cnt += 1
                ans = max(ans,cnt)
            elif c== ')':
                cnt -= 1
        return ans