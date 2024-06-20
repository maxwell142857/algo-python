class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionary = {}
        for item in s:
            dictionary[item] = dictionary.get(item,0)+1
        for item in t:
            if dictionary.get(item,0) > 0:
                dictionary[item] -= 1
            else:
                return False
        return True