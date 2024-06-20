class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            cur = happiness[i]-i
            if cur > 0:
                ans += happiness[i]-i
            else:
                break
        return ans