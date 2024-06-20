class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        l = 200
        for s in strs:
            l = min(l,len(s))
        while index < l:
            target = strs[0][index]
            for s in strs:
                if s[index] != target:
                    return strs[0][:index]
            index += 1
        return strs[0][:index]