class Solution:
    # bit manipulation
    def subsequenceSumOr(self, nums: List[int]) -> int:
        bitCnt = [0]*64
        for i in range(63):
            for num in nums:
                if num&(1<<i):
                    bitCnt[i] += 1
        
        ans = 0
        for i in range(63):
            if bitCnt[i] > 0:
                ans += 1<<i
            bitCnt[i+1] += bitCnt[i]//2
        return ans

    # bit manipulation, more elegant, but I can't see the underlying logic
    # def subsequenceSumOr(self, nums: List[int]) -> int:
    #     result = 0
    #     preSum = 0
    #     for num in nums:
    #         preSum += num
    #         result |= preSum
    #         result |= num
    #     return result