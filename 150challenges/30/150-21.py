class Solution:
    def reverseWords(self, s: str) -> str:
        split_strings = s.split()
        split_strings = split_strings[::-1]
        ans = " ".join(split_strings)
        return ans