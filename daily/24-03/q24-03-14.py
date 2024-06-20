from collections import defaultdict


class Solution:
    # preSum
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        preSum = 0
        sum2cnt = defaultdict(int)
        sum2cnt[0]=1
        cnt = 0
        for num in nums:
            preSum += num
            cnt += sum2cnt[preSum-goal]
            sum2cnt[preSum] += 1
        return cnt
    # two pointer
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        def noMoreThanSum(target):
            if target<0:
                return 0
            left = 0
            tmpSum = 0
            cnt = 0
            for right in range(n):
                tmpSum += nums[right]
                while tmpSum > target:
                    tmpSum -= nums[left]
                    left += 1
                cnt += right-left+1
            return cnt
        
        return noMoreThanSum(goal)-noMoreThanSum(goal-1)