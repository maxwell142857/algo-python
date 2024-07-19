class Solution:
    # O(n^2) TLE
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            cnt = 1
            p = i+1
            while p<n and s[p] == s[i]:
                p += 1
                cnt += 1
            while p<n and s[p] != s[i]:
                p += 1
                cnt -= 1
                if cnt == 0:
                    ans += 1
                    break
        return ans
    
    # O(n)
    def countBinarySubstrings(self, s: str) -> int:
        preCnt = 0
        curCnt = 1
        ans = 0
        curChar = s[0]
        for i in range(1,len(s)):
            if s[i] == curChar:
                curCnt += 1
                
            else:
                curChar = s[i]
                preCnt = curCnt
                curCnt = 1
            if curCnt <= preCnt:
                ans += 1
        return ans

            
