class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        pieces = s.split(" ")
        return len(pieces[-1])