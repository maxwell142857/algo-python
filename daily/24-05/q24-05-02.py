class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        negative = set(num for num in nums if num<0)
        ans = -1
        for num in nums:
            if -num in negative and num > ans:
                ans = num
        return ans
        