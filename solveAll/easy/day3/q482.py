class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        candidates = []
        for c in s:
            if c !='-':
                if c.isalpha():
                    candidates.append(c.upper())
                else:
                    candidates.append(c)
        first = len(candidates)%k
        ans = []
        if first !=0:
            ans.append(''.join(candidates[:first]))
        p = first
        while p<len(candidates):
            ans.append(''.join(candidates[p:p+k]))
            p += k
        return '-'.join(ans)