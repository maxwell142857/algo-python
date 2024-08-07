class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        oneTotal = 0
        for val in nums:
            if val == 1:
                oneTotal += 1
        nums = nums+nums
        n = len(nums)
        curOne = 0
        p = 0
        while p<oneTotal:
            if nums[p] == 1:
                curOne += 1
            p += 1
        ans = oneTotal-curOne

        while p < n:
            # delete the first element
            if nums[p-oneTotal] == 1:
                curOne -= 1
            # add the new element
            if nums[p] == 1:
                curOne += 1
            ans = min(ans,oneTotal-curOne)
            p += 1
        return ans