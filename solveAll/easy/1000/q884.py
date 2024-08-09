class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split(' ')
        words2 = s2.split(' ')
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        ans = []
        for k,v in cnt1.items():
            if v == 1 and k not in cnt2:
                ans.append(k)
        for k,v in cnt2.items():
            if v == 1 and k not in cnt1:
                ans.append(k)
        return ans