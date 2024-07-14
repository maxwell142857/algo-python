class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a)==len(b):
            if a == b:
                return -1
            else:
                return len(a)
        else:
            return max(len(a),len(b))