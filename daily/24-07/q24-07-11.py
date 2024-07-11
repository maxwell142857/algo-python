class Solution:
    # O(n^2)
    # stack
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c ==')':
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop() # remove '('
                stack.extend(tmp)
            else:
                stack.append(c)
        return ''.join(stack)
    
    # O(n)
    # Wormhole, specific to this problem
    def reverseParentheses(self, s: str) -> str:
        # match parentheses
        match = {}
        stack = []
        n = len(s)
        for i in range(n):
            c = s[i]
            if c == '(':
                stack.append(i)
            elif c== ')':
                partner = stack.pop()
                match[partner] = i
                match[i] = partner
        
        p = 0
        direction = 1
        result = []
        while p < n:
            if p in match:
                p = match[p]
                direction *= -1
            else:
                result.append(s[p])
            p += direction
        return ''.join(result)
