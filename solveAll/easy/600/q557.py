class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        ans = []
        for w in words:
            ans.append(w[::-1])
        return ' '.join(ans)