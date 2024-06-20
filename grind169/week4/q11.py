class Solution:
    # recursion with memo
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        memo = [[-1]*n for _ in range(n)] # -1 for uncheck,0 for false, 1 for true
        def check(start,end):
            # start,end is included
            nonlocal ans
            if start == end or start > end:
                return 1
            
            if memo[start+1][end] == -1:
                memo[start+1][end] = check(start+1,end)
            if memo[start][end-1] == -1:
                memo[start][end-1] = check(start,end-1)

            if memo[start+1][end-1] == -1:
                memo[start+1][end-1] = check(start+1,end-1)
            if s[start] == s[end] and memo[start+1][end-1]:
                if end-start+1 > len(ans):
                    ans = s[start:end+1]
                return 1
            else:
                return -1
            
            
        
        check(0,len(s)-1)
        return ans
    # dp
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = s[0]
        # length = 1
        for i in range(n):
            dp[i][i] = True
        # length = 2
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
                ans = s[i:i+2]
        # dp
        for l in range(3,n+1):
            for start in range(n):
                end = start+l-1
                if end >= n:
                    break
                dp[start][end] = dp[start+1][end-1] and s[start]==s[end]
                if dp[start][end] and end-start+1>len(ans):
                    ans = s[start:end+1]
        return ans

    # two pointer
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expandFromCenterOdd(index):
            left = index-1
            right = index+1
            while left>=0 and right < n and s[left]==s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        def expandFromCenterEven(index):
            left = index
            right = index+1
            while left>=0 and right < n and s[left]==s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        ans = s[0]
        for i in range(n):
            result = expandFromCenterOdd(i)
            if len(result) > len(ans):
                ans = result
        for i in range(n):
            result = expandFromCenterEven(i)
            if len(result) > len(ans):
                ans = result
        return ans