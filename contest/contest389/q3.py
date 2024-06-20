from collections import defaultdict


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c2cnt = defaultdict(int)
        for c in word:
            c2cnt[c] += 1
        frequency = []
        for val in c2cnt.values():
            if val != 0:
                frequency.append(val)
        frequency.sort()
        n = len(frequency)
        ans = sum(frequency[:n-1])
        for i in range(n-1):
            # situation i: delete first i element, then delete the tail
            cost = 0
            for j in range(i):
                cost += frequency[j]
            tmp = frequency[i:n]
            tmpN = len(tmp)
            for j in range(tmpN-1,0,-1):
                if tmp[j]-tmp[0]>k:
                    cost += tmp[j]-tmp[0]-k
                else:
                    break
            ans = min(ans,cost)
        return ans