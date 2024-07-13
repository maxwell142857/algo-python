class Solution:
    def countSegments(self, s: str) -> int:
        content = False
        cnt = 0
        for c in s:
            if c == ' ':
                if content:
                    cnt += 1
                    content = False
            else:
                content = True
        if content:
            cnt += 1
        return cnt