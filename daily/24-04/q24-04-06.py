class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        cnt = 0
        invalid = set()
        for i in range(n):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                if cnt == 0:
                    invalid.add(i)
                else:
                    cnt -= 1

        cnt = 0
        for i in range(n-1,-1,-1):
            if s[i] == ')':
                cnt += 1
            elif s[i] == '(':
                if cnt == 0:
                    invalid.add(i)
                else:
                    cnt -= 1
        ans = []
        for i in range(n):
            if i not in invalid:
                ans.append(s[i])
        return ''.join(ans)