class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])

        def twoSumClosest(left,right,val):
            nonlocal ans
            while left < right:
                curSum = nums[left]+nums[right]+val
                if abs(curSum-target) < abs(ans-target):
                    ans = curSum
                if curSum > target:
                    right -= 1
                elif curSum < target:
                    left += 1
                else:
                    return
        
        n = len(nums)
        for i in range(n):
            twoSumClosest(i+1,n-1,nums[i])
        return ans