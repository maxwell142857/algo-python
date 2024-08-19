from collections import Counter
class Solution:
    # O(n), count sort
    def minMoves(self, rooks: List[List[int]]) -> int:
        n = len(rooks)
        rVal2cnt = Counter(p[0] for p in rooks)
        cVal2cnt = Counter(p[1] for p in rooks)

        def calculateVal(counter):
            have = []
            miss = []
            for i in range(n):
                if i not in counter:
                    miss.append(i)
                for _ in range(counter[i]-1):
                    have.append(i)

            cnt = 0
            length = len(have)
            for i in range(length):
                cnt += abs(have[i]-miss[i])
            return cnt

        ans = 0
        ans += calculateVal(rVal2cnt)
        ans += calculateVal(cVal2cnt)
        return ans
    
    # O(n*log(n)), sort
    def minMoves(self, rooks: List[List[int]]) -> int:
        n = len(rooks)
        ans = 0

        rooks.sort(key = lambda x:x[0])
        for i in range(n):
            ans += abs(i-rooks[i][0])

        rooks.sort(key = lambda x:x[1])
        for i in range(n):
            ans += abs(i-rooks[i][1])

        return ans
