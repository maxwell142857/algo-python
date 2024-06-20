class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        for s in strs:
            c2cnt = [0]*26
            for c in s:
                c2cnt[ord(c)-ord('a')] += 1
            hashmap[tuple(c2cnt)].append(s)
        return list(hashmap.values())