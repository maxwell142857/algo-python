class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                last = stack[-1]
                if ord(last)-ord(c) == 32 or ord(last)-ord(c) == -32:
                    stack.pop()
                else:
                    stack.append(c)
        return ''.join(stack)