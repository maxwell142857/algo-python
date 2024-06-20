class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ids = []
        for item in strs:
            ids.append(''.join(sorted(item)))
        id2value = {}
        for index in range(len(strs)):
            id = ids[index]
            value = strs[index]
            if id in id2value:
                id2value[id].append(value)
            else:
                id2value[id] = [value]
        return list(id2value.values())