class Solution:
    # preSum+hashmap, O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        
        val2index = {}
        val2index[0] = -1
        preSum = 0
        ans = 0
        for i in range(n):
            num = nums[i]
            preSum += num
            if preSum in val2index:
                ans = max(ans,i-val2index[preSum])
            else:
                val2index[preSum] = i
        return ans
    