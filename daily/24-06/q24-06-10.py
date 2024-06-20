class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        order = heights[:]
        order.sort()
        n = len(heights)

        cnt = 0
        for i in range(n):
            if order[i] != heights[i]:
                cnt += 1
        return cnt
        