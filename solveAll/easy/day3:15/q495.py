class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        curEnd = -1
        cnt = 0
        for t in timeSeries:
            if t>curEnd:
                cnt += duration
                curEnd = t+duration-1
            else:
                cnt += t+duration-1-curEnd
                curEnd = t+duration-1
        return cnt