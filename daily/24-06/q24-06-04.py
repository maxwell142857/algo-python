class Solution:
    def longestPalindrome(self, s: str) -> int:
        c2cnt = defaultdict(int)
        for c in s:
            c2cnt[c] += 1
        odd = False
        cnt = 0
        for val in c2cnt.values():
            if val%2==0:
                cnt += val
            else:
                odd = True
                cnt += val-1
        if odd:
            return cnt+1
        else:
            return cnt