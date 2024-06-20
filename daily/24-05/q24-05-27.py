class Solution:
    # sort 
    # O(n*lgn)
    # def specialArray(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     nums.sort()
    #     for x in range(1,n+1):
    #         if n-x > 0:
    #             if nums[n-x]>=x and nums[n-x-1]<x:
    #                 return x
    #         else:
    #             if nums[n-x]>=x:
    #                 return x
    #     return -1

    # count sort+ preSum
    # O(n)
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        val2cnt = [0]*(n+1)
        for num in nums:
            if num >=n:
                val2cnt[n] += 1
            else:
                val2cnt[num] += 1
        
        preSum = [0]*(n+1)
        preSum[n] = val2cnt[n]
        for i in range(n-1,-1,-1):
            preSum[i] = preSum[i+1]+val2cnt[i]
        
        for i in range(n+1):
            if i==preSum[i]:
                return i
        return -1
