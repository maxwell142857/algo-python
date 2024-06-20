class Solution:
    # TC:O(n),SC:O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        newArray = nums[n-k:]+nums[:n-k]
        for i in range(n):
            nums[i] =  newArray[i]
    # TC:O(n),SC:O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        cnt = 0 # how many elements already in place
        k  = k%n
        startIndex = 0
        while cnt < n:
            curIndex = startIndex
            nextVal = nums[curIndex]
            while True:
                tmp = nextVal
                nextVal = nums[(curIndex+k)%n]
                nums[(curIndex+k)%n] = tmp
                curIndex = (curIndex+k)%n
                
                cnt += 1
                if curIndex == startIndex:
                    startIndex += 1
                    break
        

            


