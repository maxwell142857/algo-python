class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if len(stack) == 0:
                stack.append(item)
            else:
                last = stack[-1]
                if (last == '(' and item == ')') or \
                (last == '[' and item == ']') or \
                (last == '{' and item == '}'):
                    del stack[-1]
                else:
                    stack.append(item)
        return len(stack) == 0