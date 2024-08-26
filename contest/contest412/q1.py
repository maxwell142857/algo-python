class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n =len(nums)
        for _ in range(k):
            minVal = min(nums)
            for i in range(n):
                if nums[i] == minVal:
                    nums[i] *= multiplier
                    break
        return nums