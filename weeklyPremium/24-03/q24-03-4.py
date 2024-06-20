class Solution:
    def removeVowels(self, s: str) -> str:
        ans = ''
        vowels = 'aeiou'
        for c in s:
            if c not in vowels:
                ans += c
        return ans