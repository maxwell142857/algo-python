class Solution:
    def isValid(self, word: str) -> bool:
        number = '1234567890'
        letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        vowel = 'aeiouAEIOU'
        if len(word)<3:
            return False
        hasV  =False
        hasC = False
        for c in word:
            if c not in letters and c not in number:
                return False
            if c in vowel:
                hasV = True
            if c not in vowel and c in letters:
                hasC = True
        return hasC and hasV