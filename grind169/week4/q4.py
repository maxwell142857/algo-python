class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeroCnt = 0
        oneCnt = 0
        twoCnt = 0
        for number in nums:
            if number == 0:
                zeroCnt += 1
            elif number == 1:
                oneCnt += 1
            else:
                twoCnt += 1
        for i in range(zeroCnt):
            nums[i] = 0
        for i in range(zeroCnt,zeroCnt+oneCnt):
            nums[i] = 1
        for i in range(zeroCnt+oneCnt,n):
            nums[i] = 2
    
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0,p2 = 0,n-1
        cur = 0
        while cur <= p2:
            if nums[cur] == 0:
                if cur == p0:
                    cur += 1
                    p0 += 1
                else:
                    nums[p0],nums[cur] = nums[cur],nums[p0]
                    p0 += 1
            elif nums[cur] == 2:
                nums[p2],nums[cur] = nums[cur],nums[p2]
                p2 -= 1
            else:
                cur += 1