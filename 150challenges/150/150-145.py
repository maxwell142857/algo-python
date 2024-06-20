class Solution:
    # recursion with memo,O(n^2),failed as MLE
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        ans = [0,0]
        def check(start,end):
            nonlocal ans
            if start > end:
                return True
            if start == end:
                return True
            
            if (start,end) in memo:
                return memo[(start,end)]
            
            if (start,end-1) not in memo:
                check(start,end-1)
            if (start+1,end) not in memo:
                check(start+1,end)

            if s[start] == s[end] and check(start+1,end-1):
                memo[(start,end)] = True
                if end-start > ans[1]-ans[0]:
                    ans = [start,end]
            else:
                memo[(start,end)] = False

            return memo[(start,end)] 
        
        check(0,len(s)-1)
        return s[ans[0]:ans[1]+1]
    



    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = s[0]
        for i in range(n):
            dp[i][i] = True
        for i in range(1,n):
            if s[i-1] == s[i]:
                dp[i-1][i] = True
                ans = s[i-1:i+1]
        
        for length in range(3,n):
            for start in range(n-length+1):
                end = start+length-1
                if s[start] == s[end] and dp[start+1][end-1]:
                    dp[start][end] = True
                    ans = s[start:end+1]
        return ans
                







    # from mid generate，O(n^2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [0,0]
        for start in range(1,n):
            # check len(string)%2 == 1
            left = start-1
            right = start+1
            while left>=0 and right<n and s[left]==s[right]:
                left -= 1
                right += 1
            if right-left-2 > ans[1]-ans[0]:
                ans = [left+1,right-1]
            # check len(string)%2 ==0
            left = start-1
            right = start
            while left>=0 and right<n and s[left]==s[right]:
                left -= 1
                right += 1
            if right-left-2 > ans[1]-ans[0]:
                ans = [left+1,right-1]
        
        return s[ans[0]:ans[1]+1]