class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        index = 0
        ans = []
        while index<n and nums[index]<0:
            index += 1
        negativeIndex = index-1
        positiveIndex = index
        while negativeIndex>=0 and positiveIndex<n:
            if -nums[negativeIndex] < nums[positiveIndex]:
                ans.append(nums[negativeIndex]**2)
                negativeIndex -= 1
            else:
                ans.append(nums[positiveIndex]**2)
                positiveIndex += 1

        while negativeIndex>=0:
            ans.append(nums[negativeIndex]**2)
            negativeIndex -= 1

        while positiveIndex<n:
            ans.append(nums[positiveIndex]**2)
            positiveIndex += 1

        return ans