class Solution:
    # O（n^3)
    def strangePrinter(self, s: str) -> int:
        # remove duplication
        ss = []
        for c in s:
            if not ss or ss[-1] != c:
                ss.append(c)
        s = ''.join(ss)
        n = len(s)
        memo = [[-1]*n for _ in range(n)]

        def solve(start,end):
            
            if start > end or start>=n:
                return 0
            if start == end:
                return 1
            if memo[start][end] != -1:
                return memo[start][end]
            
            result = 1+solve(start+1,end)
            for i in range(start+1,end+1):
                if s[i] == s[start]:
                    result = min(result,solve(start,i-1)+solve(i+1,end))
            
            memo[start][end] = result
            return result
        
        return solve(0,n-1)
        
        
