class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result = 0
        for i in range(k):
            if happiness[i]-i > 0:
                result += happiness[i]-i
            else:
                break
        return result