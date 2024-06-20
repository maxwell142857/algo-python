class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
            
        left = 0
        right = n-1
        while left < right:
            mid = (left+right+1)//2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid-1

        def binarySearch(start,end):
            if start > end:
                return-1
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binarySearch(mid+1,end)
            else:
                return binarySearch(start,end-1)
            
        firstResult = binarySearch(0,left)
        if firstResult != -1:
            return firstResult
        else:
            return binarySearch(left+1,n-1)



            