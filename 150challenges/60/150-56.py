class Solution:
    def calculate(self, s: str) -> int:
        return self.dealSubstring(s)
    def dealSubstring(self,s):
        ans = 0
        n = len(s)
        operator = 1 # by default, the operator should be +
        number = 0
        index = 0
        while index < n:
            if s[index] == ' ':
                index += 1
            elif s[index] == '-':
                operator = -1
                index += 1
            elif s[index] == '+':
                operator = 1
                index += 1
            elif s[index] == '(':
                start = index+1
                bracketCnt = 1
                index += 1
                while bracketCnt > 0:
                    if s[index] == '(':
                        bracketCnt += 1
                    elif s[index] == ')':
                        bracketCnt -= 1
                    index += 1
                number = self.dealSubstring(s[start:index-1])
                ans += operator*number
            else:
                start = index
                while index < n and s[index] not in '+-() ':
                    index += 1
                number = int(s[start:index])
                ans += operator*number
        return ans
                

s = Solution()
print(s.calculate("1 +1"))
