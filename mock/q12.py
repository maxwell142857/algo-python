# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
 
# 示例 1：输入：n = 12
# 输出：3 
# 12 = 4 + 4 + 4
# f(12) = f(11)+f(1), f(8)+f(4),f(3)+f(9),f(K^2) = 1
# 12 = 9+1+1+1
# 示例 2：输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
 
# 提示：
# 1 <= n <= 10^4

class Solution:
    def numSquares(self, n: int) -> int:
        memo = [-1]*(n+1) # least number to construct i
        for i in range(10**2+1):
            if i*i<=n:
                memo[i*i] = 1

        def find(val):
            if memo[val] != -1:
                return memo[val]
            else:
                i  = 1 
                result = val # construct of all 1
                while i*i < val:
                    result = min(result,find(val-i*i)+1)
                    i += 1
                memo[val] = result
                return memo[val]
        
        return find(n)

s = Solution()
print(s.numSquares(13))