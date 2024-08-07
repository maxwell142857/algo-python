from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c2cnt = Counter(arr)
        index = 0
        for c in arr:
            if c2cnt[c] == 1:
                index += 1
            if index == k:
                return c
        return ''
