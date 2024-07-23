class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False
        index = []
        for i in range(n):
            if s[i] != goal[i]:
                index.append(i)
            
        if len(index) >2 or len(index) == 1:
                return False
        if len(index) == 2:
            i1,i2 = index
            return s[i1]==goal[i2] and s[i2]==goal[i1]
        else:
            seen = set()
            for c in s:
                if c in seen:
                    return True
                seen.add(c)