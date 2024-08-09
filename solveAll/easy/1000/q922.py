class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p0,p1 = 0,1
        while True:
            while p0<n and nums[p0]%2==0:
                p0 += 2
            while p1<n and nums[p1]%2==1:
                p1 += 2
            if p0<n and p1<n:
                nums[p0],nums[p1] = nums[p1],nums[p0]
            else:
                break
        return nums
            