class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        preSum = 0
        cnt = 0
        for num in nums:
            preSum += num
            if preSum == 0:
                cnt += 1
        return cnt