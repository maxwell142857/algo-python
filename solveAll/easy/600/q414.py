import heapq as h
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        minH = []
        for num in nums:
            if len(minH)<3 or num>minH[0]:
                h.heappush(minH,num)
            if len(minH) > 3:
                h.heappop(minH)
        if len(minH)==3:
            return minH[0]
        else:
            return max(nums)

