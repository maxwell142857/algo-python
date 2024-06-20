class Solution:
    # simulation
    # 因为运算的优先级，先对表达式按照+-分割
    # 对于子串，evaluate它的值（如果没有运算，则直接为数值；如果有，也是*/运算，则计算）
    # 最后将所有子串求和
    # def calculate(self, s: str) -> int:
    #     positive = []
    #     negative = []
    #     n = len(s)
    #     tmp = ''
    #     isPos = True
    #     for i in range(n):
    #         if s[i] == ' ':
    #             continue
    #         if s[i] not in '-+':
    #             tmp += s[i]
    #         else:
    #             if isPos:
    #                 positive.append(tmp)
    #             else:
    #                 negative.append(tmp)
    #             tmp = ''
    #             if s[i] == '+':
    #                 isPos = True
    #             else:
    #                 isPos = False
    #     if isPos:
    #         positive.append(tmp)
    #     else:
    #         negative.append(tmp)
    #     def evaluate(target):
    #         l = len(target)
    #         # first we split number and operator
    #         array = []
    #         index = 0
    #         val = 0
    #         while index < l:
    #             while index<l and target[index] not in '*/':
    #                 val = val*10+int(target[index])
    #                 index += 1
    #             array.append(str(val))
    #             val = 0
                
    #             if index == l:
    #                 break

    #             if target[index] == '*':
    #                 array.append('*')
    #                 index += 1
    #             else:
    #                 array.append('/')
    #                 index += 1
    #         # calculate the result
    #         result = int(array[0])
    #         index = 1
    #         while index < len(array):
    #             if array[index] == '*':
    #                 result *= int(array[index+1])
    #             else:
    #                 result //= int(array[index+1])
    #             index += 2
    #         return result
    
    #     ans = 0
    #     print(positive)
    #     print(negative)
    #     for p in positive:
    #         ans += evaluate(p)
    #     for ne in negative:
    #         ans -= evaluate(ne)
    #     return ans

    # stack
    # 不需要像上述方法按优先级分割，直接利用stack来实现优先级部分
    # 读完当前的数，如果这个数之前的符号是+-,则直接扔栈里
    # 如果是*/,则pop一个元素，和这个数运算后再加入
    # def calculate(self, s: str) -> int:
    #     def truncate_toward_zero(x, y):
    #         return x // y if x >= 0 else -(-x // y)
    #     s += '!' # give it a tail to guarantee the last evaluation is taken
    #     stack = []
    #     n = len(s)
    #     sign = '+'
    #     number = 0
    #     for index in range(n):
    #         if s[index] == ' ':
    #             continue
    #         if s[index] in '+-*/!':
    #             if sign == '+':
    #                 stack.append(number)
    #             elif sign == '-':
    #                 stack.append(-number)
    #             elif sign == '*':
    #                 stack.append(stack.pop()*number)
    #             else:
    #                 stack.append(truncate_toward_zero(stack.pop(),number))
    #             sign = s[index]
    #             number = 0
    #         else:
    #             number = number*10+int(s[index])
    #     return sum(stack)
    
    
    # 对上一个方法进行空间优化
    # 没必要用栈，只需要记录上一个操作数即可
    def calculate(self, s: str) -> int:
        def truncate_toward_zero(x, y):
            return x // y if x >= 0 else -(-x // y)
        s += '!' # give it a tail to guarantee the last evaluation is taken
        ans = 0
        n = len(s)
        sign = '+'
        lastNumber = 0
        number = 0
        for index in range(n):
            if s[index] == ' ':
                continue
            if s[index] in '+-*/!':

                if sign == '+':
                    ans += lastNumber
                    lastNumber = number
                elif sign == '-':
                    ans += lastNumber
                    lastNumber = -number
                elif sign == '*':
                    lastNumber *= number
                elif sign == '/':
                    lastNumber = truncate_toward_zero(lastNumber,number)
                sign = s[index]
                number = 0
            else:
                number = number*10+int(s[index])
        return ans+lastNumber
