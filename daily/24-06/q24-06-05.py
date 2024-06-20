from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        have = Counter(words[0])
        for word in words:
            cur = Counter(word)
            newHave = {}
            for k,v in have.items():
                if k in cur:
                    newHave[k] = min(v,cur[k])
            have = newHave
        
        ans = []
        for k,v in have.items():
            for _ in range(v):
                ans.append(k)
        return ans

        