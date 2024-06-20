class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for startIndex in range(m-n):
            valid = True
            for i in range(n):
                if haystack[startIndex+i] != needle[i]:
                    valid = False
                    break
            if valid:
                return startIndex
        return -1