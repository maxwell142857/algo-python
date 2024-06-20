from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        c2cnt = defaultdict(int)
        left = 0
        ans = 0
        n = len(s)
        for right in range(n):
            c = s[right]
            c2cnt[c] += 1
            while len(c2cnt) > 2:
                cLeft = s[left]
                c2cnt[cLeft] -= 1
                if c2cnt[cLeft] == 0:
                    del c2cnt[cLeft]
                left += 1
            ans = max(ans,right-left+1)
        return ans