class Solution:
    def isValid(self, s: str) -> bool:
        char2int = {}
        char2int['('] = 1
        char2int[')'] = -1
        char2int['['] = 2
        char2int[']'] = -2
        char2int['{'] = 3
        char2int['}'] = -3

        stack = []
        for c in s:
            val = char2int[c]
            if val > 0:
                stack.append(val)
            else:
                if len(stack)>0 and val+stack[-1]== 0:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                

            