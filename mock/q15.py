# Given string num representing a non-negative integer num, and an integer k, 
# return the smallest possible integer after removing k digits from num.
 
# Example 1:Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Example 2:Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

# Example 3:Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

# 431542 
# 31542,1542,142,12

# 430105
# 30105,0105,005
 
# Constraints:
# 1 <= k <= num.length <= 105
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k>=n:
            return '0'
        stack = []
        deleteCnt = 0
        for c in num:
            val = int(c)
            while deleteCnt<k and stack and stack[-1]>val:
                stack.pop()
                deleteCnt += 1
            stack.append(val)
        
        # delete from tail if k remain
        remainK = k-deleteCnt
        for _ in range(remainK):
            stack.pop()
        # delete leading zero
        l = len(stack)
        index = 0
        while index < l:
            if stack[index] != 0:
                break
            index += 1
        
        result = ''.join(str(num) for num in stack[index:])
        if not result:
            return '0'
        else:
            return result
        
# s = Solution()

# t1 = "1432219"
# t2 = "10200"
# t3 = "10"
# print(s.removeKdigits(t1,3))
# print(s.removeKdigits(t2,1))
# print(s.removeKdigits(t3,2))