# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

# Example 1:

# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.

from typing import List


class Solution:
    # two pointer + preSum
    def longestMountain(self, arr: List[int]) -> int:
        # scan from left to right, leftIncrease[i]
        # [2,1,4,7,3,2,5]
        # [0,2,1,0,0,1,0]
        # sacan from right to left, rightIncrease[i]
        # [2,1,4,7,3,2,5]
        # [0,1,0,0,1,2,0]
        # visit each position index

        # for i in range(len(arr)):
        #     arr[i] = -arr[i]

        def generateHelpArray(array):
            n = len(array)
            result = [0]*n
            index = 0
            rightIndex = 1 # exclude
            while index < n:
                while rightIndex < n and array[rightIndex] < array[rightIndex-1]:
                    rightIndex += 1
                if rightIndex == n-1 and array[rightIndex] < array[rightIndex-1]:
                    # this rightIndex should be include
                    rightIndex += 1

                while index < rightIndex:
                    result[index] = rightIndex-index-1
                    index += 1
                rightIndex += 1
            return result
        
        leftIncrease = generateHelpArray(arr)
        arr.reverse()
        rightIncrease = generateHelpArray(arr)
        rightIncrease.reverse()

        ans = 0
        
        for i in range(len(arr)):
            if leftIncrease[i] == 0 or rightIncrease[i] == 0:
                continue
            currentResult = leftIncrease[i]+rightIncrease[i]+1
            if currentResult >= 3:
                ans = max(ans,currentResult)
        return ans
    
    # simple, two pointer
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        start = 0 # include
        end = 1 # exclude
        while end < n:
            while end < n and arr[end] == arr[end-1]:
                end += 1
            start = end-1
            up,down = False,False
            while end < n and arr[end] > arr[end-1]:
                up = True
                end += 1
            while end < n and arr[end] < arr[end-1]:
                down = True
                end += 1
            if up and down:
                ans = max(ans,end-start)
            

        return ans


s = Solution()
print(s.longestMountain([2,2,2]))