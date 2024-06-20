class Solution:
    # sliding windows, fix left
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxVal = max(nums)
        n = len(nums)
        cnt = 0
        ans = 0
        left = 0

        for right in range(n):
            if nums[right] == maxVal:
                cnt += 1
            if cnt==k:
                while nums[left] != maxVal:
                    ans += n-right
                    left += 1
                ans += n-right
                left += 1
                cnt -= 1
        return ans
    
    # sliding windows, fix right
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxVal = max(nums)
        n = len(nums)
        cnt = 0
        ans = 0
        left = 0
        for right in range(n):
            if nums[right] == maxVal:
                cnt += 1
            if cnt==k:
                while nums[left] != maxVal:
                    left += 1
                left += 1
                cnt -= 1
            ans += left
                
        return ans
    # record index of maxNum
    def countSubarrays(self, nums: List[int], k: int) -> int:
        indexs = []
        n = len(nums)
        maxN = max(nums)
        ans = 0
        for i in range(n):
            if nums[i] == maxN:
                indexs.append(i)
            if len(indexs)>=k:
                ans += indexs[-k]+1
        return ans