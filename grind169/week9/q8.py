class Solution:
    # recursion with preprocessing
    # O(n)
    # def calculate(self, s: str) -> int:
    #     # delete space
    #     tmp = [c for c in s if c != ' ']
    #     s = ''.join(tmp)

    #     # get the relationship between '(' and ')'
    #     left2right = {}
    #     stack = []
    #     for i in range(len(s)):
    #         if s[i] == '(':
    #             stack.append(i)
    #         elif s[i] == ')':
    #             left2right[stack.pop()] = i
        
    #     def compute(start,end):
                    
    #         result = 0
    #         number = 0
    #         p = start
    #         isAdd = True
    #         while p <= end:
    #             if s[p] == '(':
    #                 # without preDeal
    #                 # leftIndex = p
    #                 # cnt = 1
    #                 # while cnt != 0:
    #                 #     p += 1
    #                 #     if s[p] == '(':
    #                 #         cnt += 1
    #                 #     elif s[p] == ')':
    #                 #         cnt -= 1
    #                 # # now p point to the ')'
    #                 # if isAdd:
    #                 #     result += compute(leftIndex+1,p-1)
    #                 # else:
    #                 #     result -= compute(leftIndex+1,p-1)

    #                 # with left2right, we can find it in O(1)
    #                 if isAdd:
    #                     result += compute(p+1,left2right[p]-1)
    #                 else:
    #                     result -= compute(p+1,left2right[p]-1)
    #                 p = left2right[p]+1
    #             elif s[p] in '+-':
    #                 if isAdd:
    #                     result += number
    #                 else:
    #                     result -= number
    #                 number = 0
    #                 isAdd = s[p]=='+'
    #                 p += 1
    #             else:
    #                 number *= 10
    #                 number += int(s[p])
    #                 p += 1

                
    #         if isAdd:
    #             result += number
    #         else:
    #             result -= number
    #         return result

    #     return compute(0,len(s)-1)

    # stack
    # def calculate(self, s: str) -> int:
    #     stack = []
    #     s = '('+s+')'
    #     n = len(s)
    #     p = 0
    #     val = 0
    #     while p < n:
    #         if s[p] == ' ':
    #             p += 1
    #         elif s[p] == ')':
    #             tmp = 0
    #             number = 0
    #             while stack[-1] != '(':
    #                 if stack[-1] == '+':
    #                     tmp += number
    #                     number = 0
    #                 elif stack[-1] == '-':
    #                     tmp -= number
    #                     number = 0
    #                 else:
    #                     number = stack[-1]
    #                 stack.pop()
    #             stack.pop() # remove '('
    #             stack.append(tmp+number)
    #             p += 1
                    
    #         elif s[p] in '+-(':
    #             stack.append(s[p])
    #             p += 1
    #         else:
    #             # s[p] is a number
    #             while p<n and s[p].isdigit():
    #                 val = val*10+int(s[p])
    #                 p += 1
    #             stack.append(val)
    #             val = 0
    #     return stack[-1]
    
    # stack, on going
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        val = 0
        preVal = 0
        sign = 1
        for i in range(n):
            if s[i] == ' ':
                continue
            elif s[i].isdigit():
                val = val*10+int(s[i])
            elif s[i] == '+':
                preVal += sign*val
                val = 0
                sign = 1
            elif s[i] == '-':
                preVal += sign*val
                val = 0
                sign = -1
            elif s[i] == '(':
                stack.append(preVal)
                stack.append(sign)
                preVal = 0
                val = 0
                sign = 1
            elif s[i] == ')':
                preVal += val*sign
                val = 0
                lastSign = stack.pop()
                preVal = stack.pop()+lastSign*preVal
        return preVal+val*sign
# - (3 + (4 + 5))
