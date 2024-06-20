class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            number = nums[i]
            if nums[i]<0:
                number = -nums[i]

            if nums[number-1]<0:
                ans.append(number)
            else:
                nums[number-1] = -nums[number-1]
            
        return ans
    
    # cycle sort
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 0
        while p < n:   
            val = nums[p]
            if nums[val-1] != val:
                nums[p],nums[val-1] = nums[val-1],nums[p]
            else:
                p += 1

        
        ans = []
        for i in range(n):
            if nums[i] != i+1:
                ans.append(nums[i])
        return ans
                