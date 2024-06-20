from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        target = []
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                target.append(1)
            elif nums[i+1]<nums[i]:
                target.append(-1)
            else:
                target.append(0)

        def buildNext(arr):
            result = [0]
            n = len(arr)
            for i in range(1,n):
                lastMatchLength = result[i-1]
                if arr[i] == arr[lastMatchLength]:
                    result[i]  = lastMatchLength+1
                else:
                    length = result[lastMatchLength-1]
                    if arr[length] == arr[i]:
                        result[i] = length+1
                    else:
                        result[i] = 0
            return result
        
        next = buildNext(pattern)

        def KMP(s1,s2):
            cnt = 0
            p1 = 0
            p2 = 0
            while p1 < len(s1):
                if s1[p1] == s2[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    p2 -= next[p2]
                
                if p2 == len(s2):
                    cnt += 1
                    return p1-len(s1)



def buildNext(arr):
            result = [0]
            n = len(arr)
            for i in range(1,n):
                lastMatchLength = result[i-1]
                if arr[i] == arr[lastMatchLength]:
                    result.append(lastMatchLength+1)
                else:
                    length = result[lastMatchLength-1]
                    if arr[length] == arr[i]:
                        result.append(length+1)
                    else:
                        result.append(0)
            return result
# print(buildNext('abab'))