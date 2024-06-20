class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bSearch(start,end):
            if start > end:
                return -1
            
            mid  = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bSearch(start,mid-1)
            else:
                return bSearch(mid+1,end)

        n = len(nums)
        if nums[0] > nums[n-1]:
            # break point exist
            left = 0
            right = n-1
            while left < right:
                mid = (left+right+1)//2
                if nums[left]<nums[mid]:
                    left = mid
                else:
                    right = mid-1
            # now the space is [0,left],[left+1,n-1]
            result = bSearch(0,left)
            if result != -1:
                return result
            else:
                return bSearch(left+1,n-1)
        else:
            return bSearch(0,n-1)