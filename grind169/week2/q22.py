class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()
        ans = 0
        start = 0

        for end in range(len(s)):
            if s[end] not in used:
                used.add(s[end])
            else:
                while s[start] != s[end]:
                    used.remove(s[start])
                    start += 1
                start += 1
            ans = max(ans,end-start+1)
        return ans
                
