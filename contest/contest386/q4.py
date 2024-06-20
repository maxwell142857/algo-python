class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        # exclude the endIndex
        def check(endIndex):
            # check special case:
            special = True
            last = changeIndices[endIndex-1]
            for i in range(endIndex-1):
                if changeIndices[i] == last:
                    special = False
                    break
            if special:
                copy = nums[::]
                usedCnt = 0
                for i in range(endIndex-1):
                    if copy[changeIndices[i]] != 0:
                        usedCnt += 1
                        copy[changeIndices[i]] = 0
                for num in copy:
                    usedCnt += num+1
                return usedCnt <= endIndex
            else:
                copy = nums[::]
                usedCnt = 0
                for i in range(endIndex):
                    if copy[changeIndices[i]] != 0:
                        usedCnt += 1
                        copy[changeIndices[i]] = 0
                for num in copy:
                    usedCnt += num+1
                return usedCnt <= endIndex
            
                

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