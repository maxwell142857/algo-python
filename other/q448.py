class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 0
        while p < n:
            number = nums[p]
            if nums[number-1] != number:
                nums[number-1],nums[p] = nums[p],nums[number-1]
            else:
                p += 1
        
        ans = []
        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans
