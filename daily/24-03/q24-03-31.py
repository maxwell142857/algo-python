from sortedcontainers import SortedList
class Solution:
    # brute force, O(n^2), TLE
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        n = len(nums)
        cnt = 0
        for i in range(n):
            tmpMax = -1
            tmpMin = 10**6+1
            for j in range(i,n):
                tmpMax = max(tmpMax,nums[j])
                tmpMin = min(tmpMin,nums[j])
                if tmpMax == maxK and tmpMin == minK:
                    cnt += 1
        return cnt


    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        minIndex,maxIndex = -1,-1
        outIndex = -1
        cnt = 0
        for i in range(n):
            if nums[i] == minK:
                minIndex = i
            if nums[i] == maxK:
                maxIndex = i
            if nums[i]<minK or nums[i]>maxK:
                outIndex = i
            if minIndex!=-1 and maxIndex!=-1:
                cnt += max(0,min(minIndex,maxIndex)-outIndex)
        return cnt


        