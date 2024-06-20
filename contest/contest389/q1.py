class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        record = set()
        for i in range(n-1):
            record.add(s[i:i+2])
        s = s[::-1]
        for i in range(n-1):
            if s[i:i+2] in record:
                return True
        return False