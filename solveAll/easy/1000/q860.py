class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        val2cnt = defaultdict(int)
        for b in bills:
            if b == 5:
                val2cnt[5] += 1
            elif b == 10:
                if val2cnt[5] != 0:
                    val2cnt[5] -= 1
                    val2cnt[10] += 1
                else:
                    return False
            else:
                if val2cnt[5] != 0 and val2cnt[10] != 0:
                    val2cnt[5] -= 1
                    val2cnt[10] -= 1
                    val2cnt[20] += 1
                elif val2cnt[5]>=3:
                    val2cnt[5] -= 3
                    val2cnt[20] += 1
                else:
                    return False
        return True