class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        n = len(s)
        for i in range(n):
            if s[i:]+s[:i] == goal:
                return True
        return False