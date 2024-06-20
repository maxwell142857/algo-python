class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char,0)+1
        isOdd = False
        ans = 0
        for val in hashmap.values():
            if val%2 == 1:
                isOdd = True
            ans += (val//2)*2
        if isOdd:
            return ans+1
        else:
            return ans
