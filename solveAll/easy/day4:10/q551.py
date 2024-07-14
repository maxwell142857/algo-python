class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt = Counter(s)
        if cnt['A'] >= 2:
            return False
        
        consecutive = 0
        for i in range(len(s)):
            if s[i] == 'L':
                consecutive += 1
                if consecutive >= 3:
                    return False
            else:
                consecutive = 0
        return True