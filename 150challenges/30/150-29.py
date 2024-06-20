class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            left = i+1
            right = n-1
            while left < right:
                if nums[left]+nums[right]+nums[i] == 0:
                    ans.add((nums[i],nums[left],nums[right]))
                    left += 1
                elif nums[left]+nums[right]+nums[i] > 0:
                    right -= 1
                else:
                    left += 1
        return list(ans)