class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        s2cnt = defaultdict(int)
        for i in range(0,n,k):
            s = word[i:i+k]
            s2cnt[s] += 1
        maxCnt = 0
        for val in s2cnt.values():
            maxCnt = max(maxCnt,val)
        return n//k-maxCnt