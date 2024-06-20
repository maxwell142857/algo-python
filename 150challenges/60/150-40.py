class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        convertTable = {}
        used = set()
        for index in range(len(s)):
            if s[index] not in convertTable:
                if t[index] not in used:
                    convertTable[s[index]] = t[index]
                    used.add(t[index])
                else:
                    return False
            else:
                if t[index] != convertTable[s[index]]:
                    return False
        return True