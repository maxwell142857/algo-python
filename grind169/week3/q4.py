class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def isNumber(s):
            try:
                int(s)
                return True
            except:
                return False
        
        stack = []
        for token in tokens:
            if isNumber(token):
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token =='+':
                    stack.append(num2+num1)
                elif token =='-':
                    stack.append(num2-num1)
                elif token =='*':
                    stack.append(num2*num1)
                else:
                    stack.append(int(num2/num1))
        
        return stack[0]
            
