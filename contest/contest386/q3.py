from typing import List
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        # exclude the endIndex
        def check(endIndex):
            index2lastTime = {} 
            for i in range(endIndex):
                index2lastTime[changeIndices[i]] = i+1
            if len(index2lastTime.keys()) != len(nums):
                return False
            candidates = [] # store pair(lastTime,index)
            for key,val in index2lastTime.items():
                candidates.append((val,key))
            candidates.sort()
            usedCnt = 0
            for candidate in candidates:
                totalCnt = candidate[0]-1
                needCnt = nums[candidate[1]]
                if needCnt+usedCnt <= totalCnt:
                    usedCnt += needCnt+1
                else:
                    return False
                
            return True

        n = len(changeIndices)
        # make it 0-index
        for i in range(n):
            changeIndices[i] -= 1

        # binary search to check the answer
        left = 0
        right = n
        while left < right:
            mid = (left+right)//2
            if check(mid):
                right = mid
            else:
                left = mid+1
        
        if right == n:
            if check(n):
                return n
            else:
                return -1
        else:
            return right
