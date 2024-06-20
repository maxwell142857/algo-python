class Solution:
    # hashmap
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
                
        ans = []
        for i in range(n):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            if nums[i] > 0:
                break

            seen = set()
            j = i+1
            while j < n:
                thirdNumber = -nums[i]-nums[j]
                if thirdNumber in seen:
                    ans.append([nums[i],thirdNumber,nums[j]])
                    while j+1 < n and nums[j+1] == nums[j]:
                        j += 1
                seen.add(nums[j])
                j += 1
        return ans
    
    # two pointer 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        def twoSum(start,target):
            left= start
            right = n-1
            while left < right:
                if nums[left]+nums[right] == target:
                    ans.append([-target,nums[left],nums[right]])
                    right -= 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
                    left += 1
                elif nums[left]+nums[right] > target:
                    right -= 1
                else:
                    left += 1
        
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break

            twoSum(i+1,-nums[i])
        return ans