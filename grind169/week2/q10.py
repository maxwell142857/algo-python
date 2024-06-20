class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeroCnt = 0
        for i in range(n-zeroCnt):
            if nums[i] == 0:
                zeroCnt += 1
            else:
                nums[i-zeroCnt] = nums[i]
        for i in range(n-1,n-zeroCnt-1,-1):
            nums[i] = 0
        