from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        result = []
        for num,count in count.items():
            result.append((count,num))
        result.sort(reverse=True)
        maxCount = result[0][0]
        index = 0
        ans = 0
        while index<len(result) and result[index][0] == maxCount:
            index += 1
            ans += maxCount
        return ans