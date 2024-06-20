class Solution:
    # O(n^2), TLE
    # def longestValidParentheses(self, s: str) -> int:
    #     n = len(s)
    #     ans = 0
    #     for start in range(n):
    #         cnt = 0
    #         leftCnt = 0
    #         for i in range(start,n):
    #             if s[i] == '(':
    #                 leftCnt += 1
    #             else:
    #                 if leftCnt:
    #                     leftCnt -= 1
    #                     cnt += 2
    #                 else:
    #                     break
    #             if leftCnt == 0:
    #                 ans = max(ans,cnt)
    #     return ans
    

    # stack,two pass
    # O(n)
    # 无论是思路还是实现，都简单暴力。面试时就决定是你了
    # def longestValidParentheses(self, s: str) -> int:
    #     stack = deque()
    #     n = len(s)
    #     for i in range(n):
    #         if s[i] == '(':
    #             stack.append(i)
    #         else:
    #             if stack and s[stack[-1]] == '(':
    #                 stack.pop()
    #             else:
    #                 stack.append(i)
    #     stack.appendleft(-1)
    #     stack.append(n)
    #     # now the gap between element is legal substring
    #     l = len(stack)
    #     ans = 0
    #     for i in range(l-1):
    #         ans = max(ans,stack[i+1]-stack[i]-1)
    #     return ans
    
    # stack,one pass
    # O(n)
    # 上一个方法的优化，比较巧妙，面试时估计写不出来
    # def longestValidParentheses(self, s: str) -> int:
    #     stack = [-1]
    #     n = len(s)
    #     ans = 0
    #     for i in range(n):
    #         if s[i] == '(':
    #             stack.append(i)
    #         else:
    #             stack.pop()
    #             if stack:
    #                 ans = max(ans,i-stack[-1])    
    #             else:
    #                 stack.append(i)
    #     return ans

    # dp
    # O(n)
    # 面试时能写，但细节很多，不建议写
    # def longestValidParentheses(self, s: str) -> int:
    #     n = len(s)
    #     if n==0 or n==1:
    #         return 0

    #     dp = [0]*n # dp[i] means the longest substring end in i
    #     dp[0] = 0
    #     if s[:2] == '()':
    #         dp[1] = 2

    #     for i in range(2,n):
    #         if s[i] == '(':
    #             dp[i] = 0
    #         else:
    #             # current is )
    #             if s[i-1] == '(':
    #                 dp[i] = dp[i-2]+2
    #             else:
    #                 # possible char index
    #                 index = i-dp[i-1]-1
    #                 if index == -1:
    #                     continue
    #                 c = s[index]
    #                 if c == '(':
    #                     # like this: (XXXXXXX)
    #                     dp[i] = dp[i-1]+2+dp[index-1]
    #                 else:
    #                     dp[i] = 0
    #     return max(dp)


    # scan
    # O(n)
    # 特解，很巧妙。面试时写的出来，但不好解释
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        left=right=0
        ans = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans,left+right)
            if right>left:
                left=right=0
        
        left=right=0
        for i in range(n-1,-1,-1):
            c = s[i]
            if c== '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans,left+right)
            if left>right:
                left=right=0
        return ans

        


