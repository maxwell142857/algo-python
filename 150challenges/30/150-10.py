from typing import List
class Solution:

    # dp, time complexity: O(m*n), m is the max distance for each jump, n is the size of nums
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        step = [10000]*n
        step[0] = 0
        for index,item in enumerate(nums):
            currentMax = index+item
            i = index + 1
            while i < n and i <= currentMax:
                step[i] = min(step[i],step[index] + 1)
                i += 1
        return step[n-1]
    
    # greedy, time complexity: O(n), since the dp array is increasing, we only need to record the furest we can go
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        farIndex = 0
        step = 0
        stepIndex = 0
        for index in range(len(nums)):
            farIndex = max(farIndex,index+nums[index])
            if farIndex >= n-1:
                return step+1
            if index == stepIndex:
                step += 1
                stepIndex = farIndex


        return -1