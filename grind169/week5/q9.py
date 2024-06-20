class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1324321
        # 13(2)4(3)21
        # 133(4221)
        # 1331224
        n = len(nums)
        desIndex = -1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                desIndex = i
                break
        if desIndex == -1:
            # reverse the whole array
            tmp = nums[::-1]
            for i in range(n):
                nums[i] = tmp[i]
        else:
            swapIndex = -1
            # find the first element greater than nums[desIndex]
            for i in range(n-1,-1,-1):
                if nums[i]>nums[desIndex]:
                    swapIndex = i
                    break 
            nums[desIndex],nums[swapIndex] = nums[swapIndex],nums[desIndex]
            # reverse the array[desIndex+1:]
            start = desIndex+1
            end = n-1
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
            


                