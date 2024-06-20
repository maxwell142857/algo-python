from collections import defaultdict


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        number2cnt = defaultdict(int)
        for num in nums:
            number2cnt[num] += 1
        maxFCnt = 0
        maxF = 0
        for key,val in number2cnt.items():
            if val > maxF:
                maxF = val
                maxFCnt = 1
            elif val == maxF:
                maxFCnt += 1
        return maxFCnt*maxF
