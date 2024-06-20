from collections import defaultdict
class Solution:
    # def sortColors(self, nums: List[int]) -> None:
        # val2cnt = defaultdict(int)
        # for num in nums:
        #     val2cnt[num] += 1
        
        # p = 0
        # # fill number
        # for val in range(3):
        #     cnt = val2cnt[val]
        #     while cnt:
        #         nums[p] = val
        #         cnt -= 1
        #         p += 1
    
    # Dutch National Flag algorithm
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        zeroP = 0
        twoP = n-1
        p = 0
        while p<=twoP:
            if nums[p] == 0:
                nums[zeroP],nums[p] = nums[p],nums[zeroP]
                zeroP += 1
                p += 1
            elif nums[p] == 1:
                p += 1
            else:
                nums[twoP],nums[p] = nums[p],nums[twoP]
                twoP -= 1

