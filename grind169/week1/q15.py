class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}
        for char in magazine:
            dictionary[char] = dictionary.get(char,0)+1
        for char in ransomNote:
            dictionary[char] = dictionary.get(char,0)-1
            if dictionary[char] < 0:
                return False
        return True