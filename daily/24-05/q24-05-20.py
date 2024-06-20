class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        def traverse(index,val):
            nonlocal ans
            if index == n:
                ans += val
                return 

            traverse(index+1,val^nums[index])
            traverse(index+1,val)
        traverse(0,0)
        return ans