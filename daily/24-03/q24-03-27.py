class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        n = len(nums)
        left = 0
        tmp = 1
        cnt = 0

        for right in range(n):
            tmp *= nums[right]
            while tmp > k:
                tmp //= nums[left]
                left += 1
            cnt += right-left+1
        return cnt
    


