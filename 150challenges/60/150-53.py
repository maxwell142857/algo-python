class Solution:
    def simplifyPath(self, path: str) -> str:
        pieces = path.split('/')
        stack = []
        for item in pieces:
            if item != '' or item !='.':
                if item == '..':
                    if len(stack) != 0:
                        del stack[-1]
                else:
                    stack.append(item)
        ans = '/'
        for item in stack:
            ans += item
            ans += '/'
        if ans == '/':
            return ans
        else:
            return ans[0:-1]