# Given an integer array nums and an integer k, 
# return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [4,5,0,-2,-3,1], k = 5 
#        preSum=[0,4,4,4,2,4,0]
                #0+1+2+0+3+1 =7

# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# 2 <= k <= 104
from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        number2cnt = defaultdict(int) # calculate how many times this number appear before
        number2cnt[0] = 1
        preSum = 0
        ans = 0
        for i in range(n):
            preSum += nums[i]
            preSum %= k
            ans += number2cnt[preSum]
            number2cnt[preSum] += 1
        return ans
s = Solution()
print(s.subarraysDivByK([4,5,0,-2,-3,1],5 ))
print(s.subarraysDivByK([5],9 ))
