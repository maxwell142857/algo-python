class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        used = set()
        ans = 0
        left = 0
        right = 0
        while right < n:
            if s[right] in used:
                while s[left] != s[right]:
                    used.remove(s[left])
                    left += 1
                left += 1
                ans = max(ans,right-left+1)
            else:
                used.add(s[right])
                ans = max(ans,right-left+1)
            right += 1
        return ans 
    

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        used = set()
        ans = 0
        left = 0
        for right in range(n):
            if s[right] in used:
                while s[left] != s[right]:
                    used.remove(s[left])
                    left += 1
                left += 1
            else:
                used.add(s[right])
            ans = max(ans,right-left+1)
        return ans
        
        