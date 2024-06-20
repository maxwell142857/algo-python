class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        c2cnt = defaultdict(int)
        ans = 1
        left = 0
        c2cnt[s[left]] = 1
        for right in range(1,len(s)):
            if c2cnt[s[right]]<2:
                c2cnt[s[right]] += 1
                ans = max(ans,right-left+1)
            else:
                while s[left] != s[right]:
                    c2cnt[s[left]] -= 1
                    left += 1
                left += 1
                ans = max(ans,right-left+1)
        return ans