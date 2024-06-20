class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative = []
        positive = []
        for i in range(len(nums)):
            if nums[i] < 0:
                negative.append(-nums[i])
            else:
                positive.append(nums[i])
        negative.reverse()

        result = []
        p1,p2 = 0,0
        while p1 < len(negative) and p2 < len(positive):
            if negative[p1] > positive[p2]:
                result.append(positive[p2])
                p2 += 1
            else:
                result.append(negative[p1])
                p1 += 1
        result.extend(negative[p1:])
        result.extend(positive[p2:])

        return [x**2 for x in result]