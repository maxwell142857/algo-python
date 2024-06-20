class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        s = str(num)
        for c in s:
            while stack and int(stack[-1])>int(c) and k:
                stack.pop()
                k -= 1
            stack.append(c)
        tmp = ''.join(stack)
        p = 0
        while p< len(tmp) and tmp[p] == '0':
            p += 1
        n = len(tmp)
        if n-k<=p:
            return '0'
        else:
            return tmp[p:n-k]
        