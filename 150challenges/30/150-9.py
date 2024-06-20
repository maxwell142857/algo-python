from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxDistance = 0
        for index,item in enumerate(nums):
            if index <= maxDistance:
                maxDistance = max(maxDistance,index+item)
                if maxDistance >= n-1:
                    return True
            else:
                break

        return False