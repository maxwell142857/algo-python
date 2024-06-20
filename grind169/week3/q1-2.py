class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        

        nums.sort()
        n = len(nums)
        ans  = 0
        def twoSumSamller(firstIndex):
            nonlocal ans
            left = firstIndex+1
            right = n-1
            while left < right:
                if nums[firstIndex]+nums[left]+nums[right] < target:
                    ans +=  right-left
                    left += 1
                else:
                    right -= 1


        for i in range(n):
            twoSumSamller(i)

        return ans
