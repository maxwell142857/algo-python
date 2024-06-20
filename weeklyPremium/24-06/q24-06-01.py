from collections import defaultdict
import math
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c2cnt = defaultdict(int)
        for c in s:
            c2cnt[c] += 1
        ans = len(s) # substring in length 1

        for v in c2cnt.values():
            ans += math.comb(v,2)
        return ans
