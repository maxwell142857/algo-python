class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        n = len(s)
        p = 0
        while p<n:
            tmp = s[p:min(p+k,n)]
            tmp = tmp[::-1]
            result.append(tmp)
            p += k
            if p<n:
                result.append(s[p:min(p+k,n)])
            p += k
        return ''.join(result)
