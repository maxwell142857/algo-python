from collections import defaultdict
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        val2cnt = defaultdict(int)
        for val in target:
            val2cnt[val] += 1
        for val in arr:
            val2cnt[val] -= 1
        for cnt in val2cnt.values():
            if cnt != 0:
                return False
        return True