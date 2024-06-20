class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        c2cnt = defaultdict(int)
        n = len(s)
        left = 0
        length = 0
        for right in range(n):
            c = s[right]
            c2cnt[c] += 1
            while len(c2cnt) >k:
                cLeft = s[left]
                c2cnt[cLeft] -= 1
                if c2cnt[cLeft] == 0:
                    del c2cnt[cLeft]
                left += 1
            length = max(length,right-left+1)
        return length