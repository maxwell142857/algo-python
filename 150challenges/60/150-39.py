class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}
        for item in magazine:
            dictionary[item] = dictionary.get(item,0)+1

        for target in ransomNote:
            if dictionary.get(target,0) == 0:
                return False
            else:
                dictionary[target] -= 1
        return True