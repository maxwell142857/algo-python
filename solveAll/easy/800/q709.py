class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = []
        for c in s:
            ans.append(c.lower())
        return ''.join(ans)