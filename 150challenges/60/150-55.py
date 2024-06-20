from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operator = set(['+','-','*','/'])
        for item in tokens:
            if item not in operator:
                stack.append(item)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if item =='+':
                    stack.append(first+second)
                elif item =='-':
                    stack.append(first-second)
                elif item =='*':
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))
        return stack[0]
