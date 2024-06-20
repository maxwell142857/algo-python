class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = 0
        for num in nums:
            result ^= num
        mask = 1
        while mask&result == 0:
            mask <<= 1
        # divide num into two groups
        zero = 0
        one = 0
        for num in nums:
            if num&mask:
                one ^= num
            else:
                zero ^= num
        return [zero,one]
