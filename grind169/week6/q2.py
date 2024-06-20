class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        p = 0
        while p < n:
            num = nums[p]
            if nums[num-1] != num:
                nums[num-1],nums[p] = nums[p],nums[num-1]
            else:
                if p == num-1:
                    p += 1
                else:
                    return num
        return -1
    # [1,3,4,2,2]