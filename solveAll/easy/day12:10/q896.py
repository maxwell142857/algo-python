class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        
        diff = nums[n-1]-nums[0]
        if diff == 0:
            for i in range(1,n):
                if nums[i] != nums[0]:
                    return False
            return True
        else:
            for i in range(1,n):
                if (nums[i]-nums[i-1])*diff < 0:
                    return False
            return True