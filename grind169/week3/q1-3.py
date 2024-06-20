class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = float("inf")
        nums.sort()

        def twoSumClosest(index):
            nonlocal ans
            left = index+1
            right = n-1
            while left < right:
                mySum = nums[index]+nums[left]+nums[right]
                if abs(mySum-target) < abs(ans-target):
                    ans = mySum
                if mySum > target:
                    right -= 1
                else:
                    left += 1
        
        for i in range(n):
            twoSumClosest(i)
        return ans