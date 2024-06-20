class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        n = len(nums)
        if n == 0:
            return [-1,-1]
        left = 0
        right = n-1
        # find the left
        while left < right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1
        if nums[right] == target:
            ans.append(right)
            left = right
            right = n-1
            while left < right:
                mid = (left+right+1)//2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid-1
            ans.append(left)
            return ans
        else:
            return [-1,-1]